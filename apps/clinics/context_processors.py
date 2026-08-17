from apps.clinics.models import Clinic


def clinic_branding(request):
    clinic = getattr(request, "clinic", None)
    if clinic is None and request.user.is_authenticated and request.user.is_superuser:
        slug = request.GET.get("clinic") or request.session.get("active_clinic_slug")
        if slug:
            clinic = Clinic.objects.filter(slug=slug).first()
    return {"current_clinic": clinic}
