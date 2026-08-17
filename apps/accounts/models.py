from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN = "admin", "Clinic admin"
    RECEPTION = "reception", "Reception"
    DOCTOR = "doctor", "Doctor"


class StaffUser(AbstractUser):
    """Staff account. Patients do not need an account for walk-in status."""

    clinic = models.ForeignKey(
        "clinics.Clinic",
        on_delete=models.PROTECT,
        related_name="staff",
        null=True,
        blank=True,
        help_text="Null only for platform superusers.",
    )
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RECEPTION)
    phone = models.CharField(max_length=32, blank=True)

    class Meta:
        ordering = ["username"]

    def is_clinic_admin(self) -> bool:
        return self.role == Role.ADMIN or self.is_superuser

    def is_reception(self) -> bool:
        return self.role in {Role.ADMIN, Role.RECEPTION} or self.is_superuser

    def is_doctor_role(self) -> bool:
        return self.role == Role.DOCTOR or self.is_superuser
