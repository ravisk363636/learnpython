from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.accounts.permissions import reception_required
from apps.appointments.forms import BookAppointmentForm
from apps.appointments.models import Appointment, AppointmentStatus
from apps.appointments.services import SlotUnavailable, book_appointment, check_in_appointment, iter_slots
from apps.clinics.models import Doctor
from apps.queues.signing import sign_token


@reception_required
def book(request):
    clinic = request.clinic
    if request.method == "POST":
        form = BookAppointmentForm(request.POST, clinic=clinic)
        if form.is_valid():
            try:
                appt = book_appointment(
                    doctor=form.cleaned_data["doctor"],
                    start_at=form.cleaned_data["start_at"],
                    patient_name=form.cleaned_data["patient_name"],
                    patient_phone=form.cleaned_data["patient_phone"],
                    patient_email=form.cleaned_data["patient_email"],
                    actor=request.user,
                )
                messages.success(request, f"Booked {appt.patient_name} at {appt.start_at}.")
                return redirect("appointments:book")
            except SlotUnavailable as exc:
                form.add_error("start_at", str(exc))
    else:
        form = BookAppointmentForm(clinic=clinic)
    day = timezone.localdate()
    doctors = Doctor.objects.filter(clinic=clinic, is_active=True)
    doctor_slots = [{"doctor": d, "slots": iter_slots(d, day)} for d in doctors]
    upcoming = Appointment.objects.filter(
        clinic=clinic,
        start_at__date__gte=day,
        status__in={AppointmentStatus.BOOKED, AppointmentStatus.CHECKED_IN},
    ).select_related("doctor")[:50]
    return render(
        request,
        "appointments/book.html",
        {
            "form": form,
            "upcoming": upcoming,
            "doctor_slots": doctor_slots,
            "day": day,
        },
    )


@reception_required
@require_POST
def check_in(request, appointment_id: int):
    clinic = request.clinic
    appt = get_object_or_404(Appointment, pk=appointment_id, clinic=clinic)
    try:
        token = check_in_appointment(appointment=appt, actor=request.user)
    except SlotUnavailable as exc:
        messages.error(request, str(exc))
        return redirect("appointments:book")
    messages.success(
        request,
        f"Checked in {appt.patient_name} as token {token.display_number()}. "
        f"Status path /p/{sign_token(token)}/",
    )
    return redirect("appointments:book")


@reception_required
@require_POST
def cancel_appointment(request, appointment_id: int):
    clinic = request.clinic
    appt = get_object_or_404(Appointment, pk=appointment_id, clinic=clinic)
    appt.status = AppointmentStatus.CANCELLED
    appt.save(update_fields=["status", "updated_at"])
    messages.success(request, "Appointment cancelled.")
    return redirect("appointments:book")
