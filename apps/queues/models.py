import secrets

from django.conf import settings
from django.db import models


class TokenStatus(models.TextChoices):
    WAITING = "waiting", "Waiting"
    CALLED = "called", "Called"
    IN_CONSULT = "in_consult", "In consult"
    DONE = "done", "Done"
    NO_SHOW = "no_show", "No-show"
    CANCELLED = "cancelled", "Cancelled"


class Token(models.Model):
    clinic = models.ForeignKey("clinics.Clinic", on_delete=models.CASCADE, related_name="tokens")
    doctor = models.ForeignKey("clinics.Doctor", on_delete=models.CASCADE, related_name="tokens")
    service_date = models.DateField()
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=TokenStatus.choices, default=TokenStatus.WAITING)
    patient_name = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=32, blank=True)
    patient_email = models.EmailField(blank=True)
    appointment = models.OneToOneField(
        "appointments.Appointment",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="token",
    )
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower is earlier. Reception may change this (audited).",
    )
    public_key = models.CharField(max_length=64, unique=True, db_index=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    called_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    notify_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort_order", "number"]
        constraints = [
            models.UniqueConstraint(
                fields=["clinic", "doctor", "service_date", "number"],
                name="uniq_token_per_doctor_day",
            ),
        ]
        indexes = [
            models.Index(fields=["clinic", "service_date", "status"]),
            models.Index(fields=["public_key"]),
        ]

    def save(self, *args, **kwargs):
        if not self.public_key:
            self.public_key = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

    def display_number(self) -> str:
        return f"{self.number:03d}"

    def phone_last4(self) -> str:
        digits = "".join(c for c in self.patient_phone if c.isdigit())
        if len(digits) < 4:
            return ""
        return digits[-4:]

    def __str__(self) -> str:
        return f"#{self.display_number()} {self.status}"


class TokenSequence(models.Model):
    """Row-locked counter so concurrent issue-token requests cannot share a number."""

    clinic = models.ForeignKey("clinics.Clinic", on_delete=models.CASCADE, related_name="token_sequences")
    doctor = models.ForeignKey(
        "clinics.Doctor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="token_sequences",
    )
    service_date = models.DateField()
    next_number = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["clinic", "doctor", "service_date"],
                name="uniq_seq_doctor_day",
                condition=models.Q(doctor__isnull=False),
            ),
            models.UniqueConstraint(
                fields=["clinic", "service_date"],
                name="uniq_seq_clinic_day",
                condition=models.Q(doctor__isnull=True),
            ),
        ]


class QueueEventAction(models.TextChoices):
    ISSUED = "issued", "Issued"
    CALLED = "called", "Called"
    IN_CONSULT = "in_consult", "In consult"
    DONE = "done", "Done"
    NO_SHOW = "no_show", "No-show"
    CANCELLED = "cancelled", "Cancelled"
    REORDERED = "reordered", "Reordered"
    PAUSED = "paused", "Queue paused"
    RESUMED = "resumed", "Queue resumed"
    CHECKED_IN = "checked_in", "Checked in"


class QueueEvent(models.Model):
    clinic = models.ForeignKey("clinics.Clinic", on_delete=models.CASCADE, related_name="queue_events")
    token = models.ForeignKey(
        Token,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events",
    )
    doctor = models.ForeignKey(
        "clinics.Doctor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    action = models.CharField(max_length=20, choices=QueueEventAction.choices)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
