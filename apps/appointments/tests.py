from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.accounts.models import Role, StaffUser
from apps.appointments.services import SlotUnavailable, book_appointment, check_in_appointment
from apps.clinics.models import Clinic, Doctor
from apps.queues.models import TokenStatus
from apps.queues.services import call_next, set_paused


class AppointmentMixingTests(TestCase):
    def setUp(self):
        self.clinic = Clinic.objects.create(
            name="Mix",
            slug="mix",
            appointment_priority_grace_minutes=10,
        )
        self.doctor = Doctor.objects.create(clinic=self.clinic, display_name="Dr Mix")
        self.desk = StaffUser.objects.create_user(
            username="desk_mix",
            password="correct-horse-battery-1",
            clinic=self.clinic,
            role=Role.RECEPTION,
        )

    def test_double_book_rejected(self):
        start = timezone.now() + timedelta(hours=1)
        book_appointment(
            doctor=self.doctor,
            start_at=start,
            patient_name="First",
            actor=self.desk,
        )
        with self.assertRaises(SlotUnavailable):
            book_appointment(
                doctor=self.doctor,
                start_at=start,
                patient_name="Second",
                actor=self.desk,
            )

    def test_due_appointment_called_before_walkin(self):
        from apps.queues.services import issue_token

        walk = issue_token(clinic=self.clinic, doctor=self.doctor, patient_name="Walk", actor=self.desk)
        appt = book_appointment(
            doctor=self.doctor,
            start_at=timezone.now() - timedelta(minutes=1),
            patient_name="Booked",
            actor=self.desk,
        )
        check_in_appointment(appointment=appt, actor=self.desk)
        called = call_next(doctor=self.doctor, actor=self.desk)
        self.assertEqual(called.patient_name, "Booked")
        walk.refresh_from_db()
        self.assertEqual(walk.status, TokenStatus.WAITING)

    def test_pause_blocks_call_next(self):
        from apps.queues.services import issue_token

        issue_token(clinic=self.clinic, doctor=self.doctor, patient_name="Walk", actor=self.desk)
        set_paused(doctor=self.doctor, paused=True, actor=self.desk, reason="Lunch")
        self.doctor.refresh_from_db()
        self.assertIsNone(call_next(doctor=self.doctor, actor=self.desk))
