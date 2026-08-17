from django.contrib import admin

from .models import NotificationLog


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ("channel", "destination", "success", "created_at", "clinic")
    list_filter = ("channel", "success")
    readonly_fields = ("clinic", "token", "channel", "destination", "body", "success", "error", "created_at")
