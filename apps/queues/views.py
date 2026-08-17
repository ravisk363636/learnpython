from django.conf import settings
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django_ratelimit.decorators import ratelimit

from apps.accounts.models import Role
from apps.accounts.permissions import doctor_required, reception_required, staff_required
from apps.clinics.models import Clinic, Doctor
from apps.queues.forms import IssueTokenForm
from apps.queues.models import Token, TokenStatus
from apps.queues.services import (
    call_next,
    clinic_today,
    eta_minutes,
    issue_token,
    now_serving,
    people_ahead,
    reorder_token,
    set_paused,
    set_token_status,
    waiting_list,
)
from apps.queues.signing import resolve_signed, sign_token


def _clinic(request) -> Clinic:
    clinic = request.clinic
    if clinic is None:
        raise Http404("No clinic")
    return clinic


def _doctor_for_user(request, doctor_id=None) -> Doctor:
    clinic = _clinic(request)
    qs = Doctor.objects.filter(clinic=clinic)
    if request.user.role == Role.DOCTOR and not request.user.is_superuser:
        profile = getattr(request.user, "doctor_profile", None)
        if profile is None:
            raise Http404("No doctor profile")
        return profile
    if doctor_id:
        return get_object_or_404(qs, pk=doctor_id)
    return qs.filter(is_active=True).first()


@reception_required
def issue(request):
    clinic = _clinic(request)
    if request.method == "POST":
        form = IssueTokenForm(request.POST, clinic=clinic)
        if form.is_valid():
            token = issue_token(
                clinic=clinic,
                doctor=form.cleaned_data["doctor"],
                patient_name=form.cleaned_data["patient_name"],
                patient_phone=form.cleaned_data["patient_phone"],
                patient_email=form.cleaned_data["patient_email"],
                actor=request.user,
            )
            url = request.build_absolute_uri(
                reverse("queues:patient_status", args=[sign_token(token)])
            )
            messages.success(
                request,
                f"Token {token.display_number()} issued. Patient link: {url}",
            )
            return redirect("queues:issue")
    else:
        form = IssueTokenForm(clinic=clinic)
    return render(request, "queues/issue.html", {"form": form, "clinic": clinic})


@staff_required
@require_POST
def call_next_view(request, doctor_id: int):
    doctor = _doctor_for_user(request, doctor_id)
    if doctor.queue_paused:
        messages.warning(request, f"{doctor.display_name} queue is paused.")
        return redirect("clinics:home")
    token = call_next(doctor=doctor, actor=request.user)
    if token:
        messages.success(request, f"Now serving {token.display_number()} — {token.patient_name}")
    else:
        messages.info(request, "No patients waiting.")
    return redirect("clinics:home")


@staff_required
@require_POST
def token_action(request, token_id: int):
    clinic = _clinic(request)
    token = get_object_or_404(Token, pk=token_id, clinic=clinic)
    if request.user.role == Role.DOCTOR and not request.user.is_superuser:
        profile = getattr(request.user, "doctor_profile", None)
        if profile is None or token.doctor_id != profile.id:
            raise Http404()
    action = request.POST.get("action")
    mapping = {
        "in_consult": TokenStatus.IN_CONSULT,
        "done": TokenStatus.DONE,
        "no_show": TokenStatus.NO_SHOW,
        "cancel": TokenStatus.CANCELLED,
    }
    if action == "reorder":
        if request.user.role == Role.DOCTOR and not request.user.is_superuser:
            messages.error(request, "Doctors cannot reorder the queue.")
            return redirect("clinics:home")
        try:
            new_order = int(request.POST.get("new_sort_order", "0"))
        except ValueError:
            messages.error(request, "Invalid sort order.")
            return redirect("clinics:home")
        reorder_token(token=token, new_sort_order=new_order, actor=request.user)
        messages.success(request, f"Token {token.display_number()} reordered.")
        return redirect("clinics:home")
    if action not in mapping:
        messages.error(request, "Unknown action.")
        return redirect("clinics:home")
    set_token_status(token=token, status=mapping[action], actor=request.user)
    messages.success(request, f"Token {token.display_number()} marked {mapping[action]}.")
    return redirect("clinics:home")


@doctor_required
def doctor_queue(request):
    doctor = _doctor_for_user(request)
    if doctor is None:
        raise Http404("No doctor")
    return render(
        request,
        "queues/doctor.html",
        {
            "doctor": doctor,
            "now": now_serving(doctor),
            "waiting": waiting_list(doctor),
            "today": clinic_today(doctor.clinic),
        },
    )


@doctor_required
@require_POST
def pause_queue(request, doctor_id: int):
    doctor = _doctor_for_user(request, doctor_id)
    paused = request.POST.get("paused") == "1"
    reason = request.POST.get("reason", "")[:200]
    set_paused(doctor=doctor, paused=paused, actor=request.user, reason=reason)
    messages.success(request, "Queue paused." if paused else "Queue resumed.")
    return redirect("queues:doctor_queue")


@require_GET
def tv_board(request, slug: str):
    clinic = get_object_or_404(Clinic, slug=slug)
    doctors = Doctor.objects.filter(clinic=clinic, is_active=True)
    columns = []
    for doctor in doctors:
        nxt = list(waiting_list(doctor)[:3])
        columns.append(
            {
                "doctor": doctor,
                "now": now_serving(doctor),
                "up_next": nxt,
            }
        )
    return render(
        request,
        "queues/tv.html",
        {
            "clinic": clinic,
            "columns": columns,
            "poll": settings.BOARD_POLL_SECONDS,
        },
    )


@require_GET
@ratelimit(key="ip", rate=settings.PUBLIC_STATUS_RATE, method="GET", block=True)
def patient_status(request, signed: str):
    token = resolve_signed(signed)
    if token is None:
        raise Http404("Unknown or expired link")
    return render(
        request,
        "queues/patient.html",
        {
            "token": token,
            "ahead": people_ahead(token) if token.status == TokenStatus.WAITING else 0,
            "eta": eta_minutes(token) if token.status == TokenStatus.WAITING else 0,
            "poll": settings.BOARD_POLL_SECONDS,
        },
    )


@require_GET
@ratelimit(key="ip", rate=settings.PUBLIC_STATUS_RATE, method="GET", block=True)
def patient_status_json(request, signed: str):
    token = resolve_signed(signed)
    if token is None:
        raise Http404("Unknown or expired link")
    return JsonResponse(
        {
            "number": token.display_number(),
            "status": token.status,
            "doctor": token.doctor.display_name,
            "ahead": people_ahead(token) if token.status == TokenStatus.WAITING else 0,
            "eta_minutes": eta_minutes(token) if token.status == TokenStatus.WAITING else 0,
            "paused": token.doctor.queue_paused,
        }
    )
