from django.db import models


class TokenScope(models.TextChoices):
    DOCTOR = "doctor", "Per doctor"
    CLINIC = "clinic", "Per clinic"


class Clinic(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    token_scope = models.CharField(
        max_length=16,
        choices=TokenScope.choices,
        default=TokenScope.DOCTOR,
        help_text="Whether walk-in numbers reset per doctor or shared clinic-wide.",
    )
    average_consult_minutes = models.PositiveSmallIntegerField(default=15)
    notify_when_ahead = models.PositiveSmallIntegerField(
        default=2,
        help_text="Notify the patient when this many people are ahead.",
    )
    notifications_enabled = models.BooleanField(default=False)
    appointment_priority_grace_minutes = models.PositiveSmallIntegerField(
        default=10,
        help_text="Checked-in appointments become due this many minutes before slot start.",
    )
    timezone = models.CharField(max_length=64, default="UTC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="doctors")
    staff_user = models.OneToOneField(
        "accounts.StaffUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_profile",
    )
    display_name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)
    average_consult_minutes = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Override clinic average when set.",
    )
    queue_paused = models.BooleanField(default=False)
    pause_reason = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_name"]
        unique_together = [("clinic", "display_name")]

    def __str__(self) -> str:
        return f"{self.display_name} ({self.clinic.slug})"

    def consult_minutes(self) -> int:
        return self.average_consult_minutes or self.clinic.average_consult_minutes


class Room(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="rooms")
    name = models.CharField(max_length=80)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rooms",
    )

    class Meta:
        unique_together = [("clinic", "name")]
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class WorkingHours(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="working_hours")
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="working_hours",
        help_text="Null means clinic-wide default hours.",
    )
    weekday = models.PositiveSmallIntegerField(help_text="0=Monday … 6=Sunday")
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_minutes = models.PositiveSmallIntegerField(default=15)

    class Meta:
        ordering = ["weekday", "start_time"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(end_time__gt=models.F("start_time")),
                name="hours_end_after_start",
            )
        ]

    def __str__(self) -> str:
        who = self.doctor.display_name if self.doctor_id else "clinic"
        return f"{who} wd={self.weekday} {self.start_time}-{self.end_time}"
