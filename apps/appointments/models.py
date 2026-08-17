from django.conf import settings
from django.db import models


class AppointmentStatus(models.TextChoices):
    BOOKED = "booked", "Booked"
    CHECKED_IN = "checked_in", "Checked in"
    COMPLETED = "completed", "Completed"
    NO_SHOW = "no_show", "No-show"
    CANCELLED = "cancelled", "Cancelled"


class Appointment(models.Model):
    """Holds a non-overlapping time window on a doctor's calendar."""

    clinic = models.ForeignKey("clinics.Clinic", on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey("clinics.Doctor", on_delete=models.CASCADE, related_name="appointments")
    patient_name = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=32, blank=True)
    patient_email = models.EmailField(blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.BOOKED,
    )
    notes = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_appointments",
    )

    class Meta:
        ordering = ["start_at"]
        indexes = [
            models.Index(fields=["clinic", "doctor", "start_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.patient_name} @ {self.start_at}"
