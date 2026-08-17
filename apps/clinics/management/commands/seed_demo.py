from datetime import time
import os
import secrets

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from apps.accounts.models import Role, StaffUser
from apps.clinics.models import Clinic, Doctor, Room, WorkingHours
from apps.queues.services import issue_token


class Command(BaseCommand):
    help = "Seed a demo clinic with two doctors and sample tokens. Password from QUEUELITE_SEED_PASSWORD."

    @transaction.atomic
    def handle(self, *args, **options):
        password = os.environ.get("QUEUELITE_SEED_PASSWORD", "")
        if not password:
            if os.environ.get("DJANGO_DEBUG", "0") in {"1", "true", "True"}:
                password = secrets.token_urlsafe(16)
                self.stdout.write(
                    self.style.WARNING(
                        "QUEUELITE_SEED_PASSWORD unset; generated a one-time password for DEBUG seed:"
                    )
                )
                self.stdout.write(password)
            else:
                raise CommandError("Set QUEUELITE_SEED_PASSWORD before seeding.")

        clinic, created = Clinic.objects.get_or_create(
            slug="riverside",
            defaults={
                "name": "Riverside Clinic",
                "average_consult_minutes": 12,
                "notifications_enabled": True,
                "notify_when_ahead": 2,
            },
        )
        mehta, _ = Doctor.objects.get_or_create(
            clinic=clinic,
            display_name="Dr. A. Mehta",
            defaults={"specialization": "General"},
        )
        rao, _ = Doctor.objects.get_or_create(
            clinic=clinic,
            display_name="Dr. S. Rao",
            defaults={"specialization": "Pediatrics"},
        )
        Room.objects.get_or_create(clinic=clinic, name="Room 1", defaults={"doctor": mehta})
        Room.objects.get_or_create(clinic=clinic, name="Room 2", defaults={"doctor": rao})
        for weekday in range(6):
            WorkingHours.objects.get_or_create(
                clinic=clinic,
                doctor=None,
                weekday=weekday,
                defaults={
                    "start_time": time(9, 0),
                    "end_time": time(17, 0),
                    "slot_minutes": 15,
                },
            )

        users = [
            ("riverside_admin", Role.ADMIN, None),
            ("riverside_desk", Role.RECEPTION, None),
            ("dr_mehta", Role.DOCTOR, mehta),
            ("dr_rao", Role.DOCTOR, rao),
        ]
        for username, role, doctor in users:
            user, was_new = StaffUser.objects.get_or_create(
                username=username,
                defaults={"role": role, "clinic": clinic, "email": f"{username}@example.invalid"},
            )
            if was_new:
                user.set_password(password)
                user.role = role
                user.clinic = clinic
                user.save()
            if doctor is not None and doctor.staff_user_id is None:
                doctor.staff_user = user
                doctor.save(update_fields=["staff_user"])

        if created or not clinic.tokens.exists():
            actor = StaffUser.objects.get(username="riverside_desk")
            issue_token(clinic=clinic, doctor=mehta, patient_name="Walk-in A", actor=actor)
            issue_token(clinic=clinic, doctor=mehta, patient_name="Walk-in B", actor=actor)
            issue_token(clinic=clinic, doctor=rao, patient_name="Walk-in C", actor=actor)

        self.stdout.write(self.style.SUCCESS(f"Seeded clinic '{clinic.name}' (slug={clinic.slug})."))
        self.stdout.write("Staff usernames: riverside_admin, riverside_desk, dr_mehta, dr_rao")
        self.stdout.write(f"TV board: /board/{clinic.slug}/")
        self.stdout.write(f"Today: {timezone.localdate()}")
