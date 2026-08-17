"""Optional notify-when-N-ahead. Email in dev; SMS only if provider env is set."""

from __future__ import annotations

import logging

from django.conf import settings
from django.core.mail import send_mail

from apps.notifications.models import NotificationChannel, NotificationLog
from apps.queues.models import Token, TokenStatus

logger = logging.getLogger(__name__)


def notify_if_close(doctor) -> None:
    clinic = doctor.clinic
    if not clinic.notifications_enabled:
        return
    waiting = list(
        Token.objects.filter(
            doctor=doctor,
            status=TokenStatus.WAITING,
            notify_sent=False,
        ).order_by("sort_order", "issued_at")
    )
    threshold = clinic.notify_when_ahead
    for index, token in enumerate(waiting):
        if index <= threshold and (token.patient_email or token.patient_phone):
            _send(token, people_ahead=index)


def _send(token: Token, people_ahead: int) -> None:
    body = (
        f"Clinic {token.clinic.name}: you are approximately {people_ahead} "
        f"in line. Token {token.display_number()} for {token.doctor.display_name}."
    )
    if token.patient_email:
        try:
            send_mail(
                subject=f"Token {token.display_number()} — you are near the front",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[token.patient_email],
                fail_silently=False,
            )
            NotificationLog.objects.create(
                clinic=token.clinic,
                token=token,
                channel=NotificationChannel.EMAIL,
                destination=token.patient_email,
                body=body,
                success=True,
            )
        except Exception as exc:  # noqa: BLE001 — log and continue
            logger.warning("email notify failed: %s", exc)
            NotificationLog.objects.create(
                clinic=token.clinic,
                token=token,
                channel=NotificationChannel.EMAIL,
                destination=token.patient_email,
                body=body,
                success=False,
                error=str(exc)[:240],
            )
    if token.patient_phone:
        _maybe_sms(token, body)
    token.notify_sent = True
    token.save(update_fields=["notify_sent", "updated_at"])


def _maybe_sms(token: Token, body: str) -> None:
    if not settings.SMS_PROVIDER:
        return
    if settings.SMS_PROVIDER.lower() != "twilio":
        NotificationLog.objects.create(
            clinic=token.clinic,
            token=token,
            channel=NotificationChannel.SMS,
            destination=_mask_phone(token.patient_phone),
            body=body,
            success=False,
            error="Unknown SMS_PROVIDER",
        )
        return
    if not (settings.TWILIO_ACCOUNT_SID and settings.TWILIO_AUTH_TOKEN and settings.TWILIO_FROM_NUMBER):
        NotificationLog.objects.create(
            clinic=token.clinic,
            token=token,
            channel=NotificationChannel.SMS,
            destination=_mask_phone(token.patient_phone),
            body=body,
            success=False,
            error="Twilio credentials not configured",
        )
        return
    try:
        from urllib.request import Request, urlopen
        import base64
        import json

        url = f"https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json"
        data = (
            f"To={token.patient_phone}&From={settings.TWILIO_FROM_NUMBER}&Body={body}"
        ).encode()
        auth = base64.b64encode(
            f"{settings.TWILIO_ACCOUNT_SID}:{settings.TWILIO_AUTH_TOKEN}".encode()
        ).decode()
        req = Request(url, data=data, method="POST")
        req.add_header("Authorization", f"Basic {auth}")
        with urlopen(req, timeout=10) as resp:  # noqa: S310 — Twilio API only
            json.loads(resp.read().decode())
        NotificationLog.objects.create(
            clinic=token.clinic,
            token=token,
            channel=NotificationChannel.SMS,
            destination=_mask_phone(token.patient_phone),
            body=body,
            success=True,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("sms notify failed: %s", exc)
        NotificationLog.objects.create(
            clinic=token.clinic,
            token=token,
            channel=NotificationChannel.SMS,
            destination=_mask_phone(token.patient_phone),
            body=body,
            success=False,
            error=str(exc)[:240],
        )


def _mask_phone(phone: str) -> str:
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) < 4:
        return "***"
    return f"***{digits[-4:]}"
