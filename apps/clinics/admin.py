from django.contrib import admin

from .models import Clinic, Doctor, Room, WorkingHours


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "token_scope", "notifications_enabled")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("display_name", "clinic", "is_active", "queue_paused")
    list_filter = ("clinic", "is_active")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "clinic", "doctor")


@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ("clinic", "doctor", "weekday", "start_time", "end_time")
