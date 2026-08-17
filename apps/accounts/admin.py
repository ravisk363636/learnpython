from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StaffUser


@admin.register(StaffUser)
class StaffUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Clinic", {"fields": ("clinic", "role", "phone")}),
    )
    list_display = ("username", "clinic", "role", "is_active")
    list_filter = ("role", "clinic")
