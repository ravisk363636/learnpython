"""Walk-in token allocation and call-next mixing.

Mixing rule (appointments vs walk-ins)
--------------------------------------
Appointments reserve a **time window** on a doctor's calendar (start_at → end_at).
They do **not** consume a walk-in token number at booking time. That keeps slot
booking independent of the day's walk-in counter.

When reception checks an appointment in, the patient is issued the next real
token number (same allocator as walk-ins) and the token is linked to the
appointment.

**Call next** order for a doctor:

1. Waiting tokens with an appointment whose slot is **due**
   (now >= start_at − clinic.appointment_priority_grace_minutes), ordered by
   ``sort_order``, then ``issued_at``.
2. Otherwise the oldest waiting walk-in / early-check-in token by
   ``sort_order``, then ``issued_at``.

Reception may change ``sort_order``; that is always written to ``QueueEvent``.
"""

from __future__ import annotations

import threading
import time
from datetime import date, datetime, timedelta

from django.db import IntegrityError, OperationalError, connection, transaction
from django.utils import timezone

from apps.appointments.models import Appointment, AppointmentStatus
from apps.clinics.models import Clinic, Doctor, TokenScope
from apps.notifications.services import notify_if_close
from apps.queues.models import (
    QueueEvent,
    QueueEventAction,
    Token,
    TokenSequence,
    TokenStatus,
)


def clinic_today(clinic: Clinic) -> date:
    tz = timezone.get_current_timezone()
    return timezone.now().astimezone(tz).date()


def _lock_sequence(clinic: Clinic, doctor: Doctor, service_date: date) -> TokenSequence:
    seq_doctor = doctor if clinic.token_scope == TokenScope.DOCTOR else None
    while True:
        qs = TokenSequence.objects.select_for_update()
        if seq_doctor is None:
            seq = qs.filter(clinic=clinic, doctor__isnull=True, service_date=service_date).first()
        else:
            seq = qs.filter(clinic=clinic, doctor=seq_doctor, service_date=service_date).first()
        if seq:
            return seq
        try:
            return TokenSequence.objects.create(
                clinic=clinic,
                doctor=seq_doctor,
                service_date=service_date,
                next_number=1,
            )
        except IntegrityError:
            continue


_sqlite_alloc_lock = threading.Lock()


def issue_token(
    *,
    clinic: Clinic,
    doctor: Doctor,
    patient_name: str,
    actor,
    patient_phone: str = "",
    patient_email: str = "",
    appointment: Appointment | None = None,
    service_date: date | None = None,
) -> Token:
    if doctor.clinic_id != clinic.id:
        raise ValueError("Doctor does not belong to this clinic.")
    service_date = service_date or clinic_today(clinic)
    if connection.vendor == "sqlite":
        with _sqlite_alloc_lock:
            return _allocate_token(
                clinic=clinic,
                doctor=doctor,
                patient_name=patient_name,
                actor=actor,
                patient_phone=patient_phone,
                patient_email=patient_email,
                appointment=appointment,
                service_date=service_date,
            )
    return _allocate_token(
        clinic=clinic,
        doctor=doctor,
        patient_name=patient_name,
        actor=actor,
        patient_phone=patient_phone,
        patient_email=patient_email,
        appointment=appointment,
        service_date=service_date,
    )


def _allocate_token(
    *,
    clinic: Clinic,
    doctor: Doctor,
    patient_name: str,
    actor,
    patient_phone: str,
    patient_email: str,
    appointment: Appointment | None,
    service_date: date,
) -> Token:
    last_error: Exception | None = None
    for attempt in range(24):
        try:
            with transaction.atomic():
                seq = _lock_sequence(clinic, doctor, service_date)
                number = seq.next_number
                seq.next_number = number + 1
                seq.save(update_fields=["next_number"])
                token = Token.objects.create(
                    clinic=clinic,
                    doctor=doctor,
                    service_date=service_date,
                    number=number,
                    patient_name=patient_name.strip(),
                    patient_phone=patient_phone.strip(),
                    patient_email=patient_email.strip(),
                    appointment=appointment,
                    sort_order=number * 10,
                    status=TokenStatus.WAITING,
                )
                QueueEvent.objects.create(
                    clinic=clinic,
                    token=token,
                    doctor=doctor,
                    actor=actor,
                    action=QueueEventAction.CHECKED_IN if appointment else QueueEventAction.ISSUED,
                    metadata={
                        "number": number,
                        "appointment_id": appointment.pk if appointment else None,
                    },
                )
                return token
        except IntegrityError as exc:
            last_error = exc
            time.sleep(0.02 * (attempt + 1))
            continue
        except OperationalError as exc:
            last_error = exc
            if "locked" not in str(exc).lower() and "busy" not in str(exc).lower():
                raise
            time.sleep(0.05 * (attempt + 1))
            continue
    raise last_error or IntegrityError("Could not allocate a unique token number.")


def _is_due_appointment(token: Token, now: datetime, clinic: Clinic) -> bool:
    if not token.appointment_id:
        return False
    appt = token.appointment
    if appt.status == AppointmentStatus.CANCELLED:
        return False
    grace = timedelta(minutes=clinic.appointment_priority_grace_minutes)
    return now >= (appt.start_at - grace)


def select_next_waiting(doctor: Doctor, now: datetime | None = None) -> Token | None:
    now = now or timezone.now()
    clinic = doctor.clinic
    waiting = list(
        Token.objects.select_related("appointment")
        .filter(
            doctor=doctor,
            service_date=clinic_today(clinic),
            status=TokenStatus.WAITING,
        )
        .order_by("sort_order", "issued_at", "number")
    )
    due = [t for t in waiting if _is_due_appointment(t, now, clinic)]
    if due:
        return due[0]
    return waiting[0] if waiting else None


@transaction.atomic
def call_next(*, doctor: Doctor, actor) -> Token | None:
    Doctor.objects.select_for_update().get(pk=doctor.pk)
    if doctor.queue_paused:
        return None
    token = select_next_waiting(doctor)
    if token is None:
        return None
    token.status = TokenStatus.CALLED
    token.called_at = timezone.now()
    token.save(update_fields=["status", "called_at", "updated_at"])
    QueueEvent.objects.create(
        clinic=doctor.clinic,
        token=token,
        doctor=doctor,
        actor=actor,
        action=QueueEventAction.CALLED,
        metadata={"number": token.number},
    )
    notify_if_close(doctor)
    return token


@transaction.atomic
def set_token_status(*, token: Token, status: str, actor, metadata: dict | None = None) -> Token:
    token.status = status
    token.save(update_fields=["status", "updated_at"])
    action_map = {
        TokenStatus.IN_CONSULT: QueueEventAction.IN_CONSULT,
        TokenStatus.DONE: QueueEventAction.DONE,
        TokenStatus.NO_SHOW: QueueEventAction.NO_SHOW,
        TokenStatus.CANCELLED: QueueEventAction.CANCELLED,
        TokenStatus.CALLED: QueueEventAction.CALLED,
        TokenStatus.WAITING: QueueEventAction.ISSUED,
    }
    QueueEvent.objects.create(
        clinic=token.clinic,
        token=token,
        doctor=token.doctor,
        actor=actor,
        action=action_map.get(status, QueueEventAction.ISSUED),
        metadata=metadata or {},
    )
    if status in {TokenStatus.DONE, TokenStatus.NO_SHOW, TokenStatus.CANCELLED} and token.appointment_id:
        appt_status = {
            TokenStatus.DONE: AppointmentStatus.COMPLETED,
            TokenStatus.NO_SHOW: AppointmentStatus.NO_SHOW,
            TokenStatus.CANCELLED: AppointmentStatus.CANCELLED,
        }[status]
        Appointment.objects.filter(pk=token.appointment_id).update(status=appt_status)
    notify_if_close(token.doctor)
    return token


@transaction.atomic
def reorder_token(*, token: Token, new_sort_order: int, actor) -> Token:
    old = token.sort_order
    token.sort_order = new_sort_order
    token.save(update_fields=["sort_order", "updated_at"])
    QueueEvent.objects.create(
        clinic=token.clinic,
        token=token,
        doctor=token.doctor,
        actor=actor,
        action=QueueEventAction.REORDERED,
        metadata={"from": old, "to": new_sort_order},
    )
    return token


@transaction.atomic
def set_paused(*, doctor: Doctor, paused: bool, actor, reason: str = "") -> Doctor:
    doctor.queue_paused = paused
    doctor.pause_reason = reason if paused else ""
    doctor.save(update_fields=["queue_paused", "pause_reason", "updated_at"])
    QueueEvent.objects.create(
        clinic=doctor.clinic,
        doctor=doctor,
        actor=actor,
        action=QueueEventAction.PAUSED if paused else QueueEventAction.RESUMED,
        metadata={"reason": reason},
    )
    return doctor


def people_ahead(token: Token) -> int:
    return Token.objects.filter(
        doctor=token.doctor,
        service_date=token.service_date,
        status=TokenStatus.WAITING,
        sort_order__lt=token.sort_order,
    ).count()


def eta_minutes(token: Token) -> int:
    ahead = people_ahead(token)
    minutes = token.doctor.consult_minutes()
    in_consult = Token.objects.filter(
        doctor=token.doctor,
        service_date=token.service_date,
        status__in={TokenStatus.CALLED, TokenStatus.IN_CONSULT},
    ).count()
    return (ahead + max(in_consult, 0)) * minutes


def now_serving(doctor: Doctor) -> Token | None:
    return (
        Token.objects.filter(
            doctor=doctor,
            service_date=clinic_today(doctor.clinic),
            status__in={TokenStatus.CALLED, TokenStatus.IN_CONSULT},
        )
        .order_by("-called_at", "-updated_at")
        .first()
    )


def waiting_list(doctor: Doctor):
    return Token.objects.filter(
        doctor=doctor,
        service_date=clinic_today(doctor.clinic),
        status=TokenStatus.WAITING,
    ).order_by("sort_order", "issued_at")
