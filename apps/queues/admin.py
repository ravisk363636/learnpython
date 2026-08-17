from django.contrib import admin

from .models import QueueEvent, Token, TokenSequence


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("number", "doctor", "service_date", "status", "patient_name")
    list_filter = ("clinic", "status", "service_date")


@admin.register(TokenSequence)
class TokenSequenceAdmin(admin.ModelAdmin):
    list_display = ("clinic", "doctor", "service_date", "next_number")


@admin.register(QueueEvent)
class QueueEventAdmin(admin.ModelAdmin):
    list_display = ("action", "clinic", "token", "actor", "created_at")
    list_filter = ("action", "clinic")
    readonly_fields = ("clinic", "token", "doctor", "actor", "action", "metadata", "created_at")
