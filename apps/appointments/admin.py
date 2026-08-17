from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "doctor", "start_at", "status")
    list_filter = ("clinic", "status")
