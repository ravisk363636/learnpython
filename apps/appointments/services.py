"""Appointment slot booking with overlap prevention."""

from __future__ import annotations

from datetime import datetime, timedelta

from django.db import transaction
from django.utils import timezone

from apps.appointments.models import Appointment, AppointmentStatus
from apps.clinics.models import Doctor, WorkingHours
from apps.queues.services import issue_token


class SlotUnavailable(Exception):
    pass


def _overlaps(doctor: Doctor, start: datetime, end: datetime, exclude_id: int | None = None) -> bool:
    qs = Appointment.objects.filter(
        doctor=doctor,
        status__in={AppointmentStatus.BOOKED, AppointmentStatus.CHECKED_IN},
        start_at__lt=end,
        end_at__gt=start,
    )
    if exclude_id:
        qs = qs.exclude(pk=exclude_id)
    return qs.exists()


def hours_for(doctor: Doctor, weekday: int) -> WorkingHours | None:
    specific = WorkingHours.objects.filter(doctor=doctor, weekday=weekday).first()
    if specific:
        return specific
    return WorkingHours.objects.filter(clinic=doctor.clinic, doctor__isnull=True, weekday=weekday).first()


def iter_slots(doctor: Doctor, day) -> list[datetime]:
    hours = hours_for(doctor, day.weekday())
    if not hours:
        return []
    tz = timezone.get_current_timezone()
    start = timezone.make_aware(datetime.combine(day, hours.start_time), tz)
    end = timezone.make_aware(datetime.combine(day, hours.end_time), tz)
    step = timedelta(minutes=hours.slot_minutes)
    consult = timedelta(minutes=doctor.consult_minutes())
    slots = []
    cursor = start
    now = timezone.now()
    while cursor + consult <= end:
        taken = _overlaps(doctor, cursor, cursor + consult)
        if cursor >= now and not taken:
            slots.append(cursor)
        cursor += step
    return slots


@transaction.atomic
def book_appointment(
    *,
    doctor: Doctor,
    start_at: datetime,
    patient_name: str,
    actor,
    patient_phone: str = "",
    patient_email: str = "",
    notes: str = "",
) -> Appointment:
    Doctor.objects.select_for_update().get(pk=doctor.pk)
    end_at = start_at + timedelta(minutes=doctor.consult_minutes())
    if _overlaps(doctor, start_at, end_at):
        raise SlotUnavailable("That slot is already booked.")
    return Appointment.objects.create(
        clinic=doctor.clinic,
        doctor=doctor,
        patient_name=patient_name.strip(),
        patient_phone=patient_phone.strip(),
        patient_email=patient_email.strip(),
        start_at=start_at,
        end_at=end_at,
        notes=notes,
        created_by=actor,
        status=AppointmentStatus.BOOKED,
    )


@transaction.atomic
def check_in_appointment(*, appointment: Appointment, actor):
    if appointment.status != AppointmentStatus.BOOKED:
        raise SlotUnavailable("Appointment cannot be checked in.")
    Doctor.objects.select_for_update().get(pk=appointment.doctor_id)
    token = issue_token(
        clinic=appointment.clinic,
        doctor=appointment.doctor,
        patient_name=appointment.patient_name,
        patient_phone=appointment.patient_phone,
        patient_email=appointment.patient_email,
        actor=actor,
        appointment=appointment,
    )
    appointment.status = AppointmentStatus.CHECKED_IN
    appointment.save(update_fields=["status", "updated_at"])
    return token
