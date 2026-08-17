from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import Role, StaffUser
from apps.clinics.models import Clinic, Doctor


class RbacTests(TestCase):
    def setUp(self):
        self.clinic_a = Clinic.objects.create(name="Alpha", slug="alpha")
        self.clinic_b = Clinic.objects.create(name="Beta", slug="beta")
        self.doc_a = Doctor.objects.create(clinic=self.clinic_a, display_name="Dr A")
        self.doc_b = Doctor.objects.create(clinic=self.clinic_b, display_name="Dr B")
        self.admin_a = StaffUser.objects.create_user(
            username="admin_a", password="correct-horse-battery-1", clinic=self.clinic_a, role=Role.ADMIN
        )
        self.desk_a = StaffUser.objects.create_user(
            username="desk_a", password="correct-horse-battery-1", clinic=self.clinic_a, role=Role.RECEPTION
        )
        self.desk_b = StaffUser.objects.create_user(
            username="desk_b", password="correct-horse-battery-1", clinic=self.clinic_b, role=Role.RECEPTION
        )
        self.doctor_a = StaffUser.objects.create_user(
            username="doctor_a", password="correct-horse-battery-1", clinic=self.clinic_a, role=Role.DOCTOR
        )
        self.doc_a.staff_user = self.doctor_a
        self.doc_a.save()

    def test_anonymous_redirected_to_login(self):
        response = self.client.get(reverse("clinics:home"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_reception_cannot_open_setup(self):
        self.client.force_login(self.desk_a)
        response = self.client.get(reverse("clinics:setup"))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_open_setup(self):
        self.client.force_login(self.admin_a)
        response = self.client.get(reverse("clinics:setup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alpha")
        self.assertNotContains(response, "Dr B")

    def test_reception_cannot_issue_other_clinic_doctor(self):
        self.client.force_login(self.desk_a)
        response = self.client.post(
            reverse("queues:issue"),
            {
                "doctor": self.doc_b.pk,
                "patient_name": "Eve",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.doc_b.tokens.exists())

    def test_desk_b_home_has_no_clinic_a_doctors(self):
        self.client.force_login(self.desk_b)
        response = self.client.get(reverse("clinics:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr B")
        self.assertNotContains(response, "Dr A")

    def test_doctor_cannot_see_other_clinic_token_action(self):
        from apps.queues.services import issue_token

        token = issue_token(
            clinic=self.clinic_b,
            doctor=self.doc_b,
            patient_name="Secret",
            actor=self.desk_b,
        )
        self.client.force_login(self.doctor_a)
        response = self.client.post(
            reverse("queues:token_action", args=[token.pk]),
            {"action": "done"},
        )
        self.assertEqual(response.status_code, 404)
        token.refresh_from_db()
        self.assertEqual(token.status, "waiting")
