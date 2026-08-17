import threading

from django.db import connection
from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from apps.accounts.models import Role, StaffUser
from apps.clinics.models import Clinic, Doctor
from apps.queues.models import Token
from apps.queues.services import call_next, issue_token
from apps.queues.signing import sign_token


class ConcurrentIssueTests(TransactionTestCase):
    def setUp(self):
        self.clinic = Clinic.objects.create(name="Lock Clinic", slug="lock")
        self.doctor = Doctor.objects.create(clinic=self.clinic, display_name="Dr Lock")
        self.actor = StaffUser.objects.create_user(
            username="desk_lock",
            password="correct-horse-battery-1",
            clinic=self.clinic,
            role=Role.RECEPTION,
        )

    def test_parallel_issue_token_unique_numbers(self):
        n = 12
        errors = []

        def worker(i):
            try:
                issue_token(
                    clinic=self.clinic,
                    doctor=self.doctor,
                    patient_name=f"P{i}",
                    actor=self.actor,
                )
            except Exception as exc:  # noqa: BLE001
                errors.append(exc)
            finally:
                connection.close()

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(n)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(errors, [])
        numbers = list(Token.objects.filter(doctor=self.doctor).values_list("number", flat=True))
        self.assertEqual(len(numbers), n)
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertEqual(sorted(numbers), list(range(1, n + 1)))


class PublicSurfaceTests(TestCase):
    def setUp(self):
        self.clinic = Clinic.objects.create(name="Public Clinic", slug="public")
        self.doctor = Doctor.objects.create(clinic=self.clinic, display_name="Dr Public")
        self.desk = StaffUser.objects.create_user(
            username="desk_pub",
            password="correct-horse-battery-1",
            clinic=self.clinic,
            role=Role.RECEPTION,
        )
        self.t1 = issue_token(
            clinic=self.clinic,
            doctor=self.doctor,
            patient_name="Anita Sharma",
            actor=self.desk,
            patient_phone="+15550199",
        )
        self.t2 = issue_token(
            clinic=self.clinic, doctor=self.doctor, patient_name="Bala Kumar", actor=self.desk
        )
        call_next(doctor=self.doctor, actor=self.desk)

    def test_tv_shows_numbers_not_names_or_phones(self):
        url = reverse("queues:tv_board", args=["public"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.t1.display_number())
        self.assertNotContains(response, "Anita")
        self.assertNotContains(response, "Sharma")
        self.assertNotContains(response, "Bala")
        self.assertNotContains(response, "15550199")
        self.assertNotContains(response, "+1555")

    def test_patient_link_does_not_enumerate(self):
        signed = sign_token(self.t1)
        ok = self.client.get(reverse("queues:patient_status", args=[signed]))
        self.assertEqual(ok.status_code, 200)
        self.assertContains(ok, self.t1.display_number())
        self.assertNotContains(ok, "Bala")
        self.assertEqual(self.client.get("/token/1/").status_code, 404)
        self.assertEqual(self.client.get("/p/1/").status_code, 404)
        self.assertEqual(self.client.get(f"/p/{self.t1.pk}/").status_code, 404)
        self.assertEqual(
            self.client.get(reverse("queues:patient_status", args=["not-a-real-signature"])).status_code,
            404,
        )

    def test_staff_home_shows_names(self):
        self.client.force_login(self.desk)
        response = self.client.get(reverse("clinics:home"))
        self.assertContains(response, "Anita Sharma")
