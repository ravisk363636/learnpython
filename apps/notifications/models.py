from django.db import models


class NotificationChannel(models.TextChoices):
    EMAIL = "email", "Email"
    SMS = "sms", "SMS"


class NotificationLog(models.Model):
    clinic = models.ForeignKey("clinics.Clinic", on_delete=models.CASCADE, related_name="notification_logs")
    token = models.ForeignKey("queues.Token", on_delete=models.CASCADE, related_name="notifications")
    channel = models.CharField(max_length=10, choices=NotificationChannel.choices)
    destination = models.CharField(max_length=120)
    body = models.TextField()
    success = models.BooleanField(default=True)
    error = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
