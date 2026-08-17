from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from apps.accounts.models import Role
from apps.accounts.permissions import admin_required, clinic_required
from apps.clinics.forms import ClinicSetupForm, DoctorForm, RoomForm, StaffInviteForm, WorkingHoursForm
from apps.clinics.models import Clinic, Doctor, Room, WorkingHours
from apps.queues.services import clinic_today, now_serving, waiting_list


@clinic_required
def home(request):
    clinic = request.clinic
    if clinic is None:
        if request.user.is_superuser:
            return redirect("admin:index")
        raise PermissionDenied("Staff must belong to a clinic.")
    if request.user.role == Role.DOCTOR and getattr(request.user, "doctor_profile", None):
        return redirect("queues:doctor_queue")
    doctors = Doctor.objects.filter(clinic=clinic, is_active=True)
    boards = []
    for doctor in doctors:
        boards.append(
            {
                "doctor": doctor,
                "now": now_serving(doctor),
                "waiting": waiting_list(doctor)[:8],
            }
        )
    return render(
        request,
        "clinics/home.html",
        {"clinic": clinic, "boards": boards, "today": clinic_today(clinic)},
    )


@admin_required
def setup(request):
    clinic = request.clinic
    if request.method == "POST" and request.POST.get("form") == "clinic":
        form = ClinicSetupForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            messages.success(request, "Clinic settings saved.")
            return redirect("clinics:setup")
    else:
        form = ClinicSetupForm(instance=clinic)
    return render(
        request,
        "clinics/setup.html",
        {
            "clinic": clinic,
            "form": form,
            "doctor_form": DoctorForm(),
            "room_form": RoomForm(clinic=clinic),
            "hours_form": WorkingHoursForm(clinic=clinic),
            "staff_form": StaffInviteForm(clinic=clinic),
            "doctors": Doctor.objects.filter(clinic=clinic),
            "rooms": Room.objects.filter(clinic=clinic),
            "hours": WorkingHours.objects.filter(clinic=clinic),
            "staff": clinic.staff.all(),
        },
    )


@admin_required
@require_POST
def add_doctor(request):
    clinic = request.clinic
    form = DoctorForm(request.POST)
    if form.is_valid():
        doctor = form.save(commit=False)
        doctor.clinic = clinic
        doctor.save()
        messages.success(request, "Doctor added.")
    else:
        messages.error(request, "Could not add doctor.")
    return redirect("clinics:setup")


@admin_required
@require_POST
def add_room(request):
    clinic = request.clinic
    form = RoomForm(request.POST, clinic=clinic)
    if form.is_valid():
        room = form.save(commit=False)
        room.clinic = clinic
        room.save()
        messages.success(request, "Room added.")
    else:
        messages.error(request, "Could not add room.")
    return redirect("clinics:setup")


@admin_required
@require_POST
def add_hours(request):
    clinic = request.clinic
    form = WorkingHoursForm(request.POST, clinic=clinic)
    if form.is_valid():
        hours = form.save(commit=False)
        hours.clinic = clinic
        hours.save()
        messages.success(request, "Hours added.")
    else:
        messages.error(request, form.errors.as_text())
    return redirect("clinics:setup")


@admin_required
@require_POST
def add_staff(request):
    clinic = request.clinic
    form = StaffInviteForm(request.POST, clinic=clinic)
    if form.is_valid():
        form.save()
        messages.success(request, "Staff account created.")
    else:
        messages.error(request, form.errors.as_text())
    return redirect("clinics:setup")
