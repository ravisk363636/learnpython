from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from apps.accounts.models import Role


def clinic_required(view):
    @login_required
    @wraps(view)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.clinic_id:
            raise PermissionDenied("Staff must belong to a clinic.")
        return view(request, *args, **kwargs)

    return wrapped


def roles_required(*roles: str):
    def decorator(view):
        @clinic_required
        @wraps(view)
        def wrapped(request, *args, **kwargs):
            if request.user.is_superuser:
                return view(request, *args, **kwargs)
            if request.user.role not in roles:
                raise PermissionDenied
            return view(request, *args, **kwargs)

        return wrapped

    return decorator


admin_required = roles_required(Role.ADMIN)
reception_required = roles_required(Role.ADMIN, Role.RECEPTION)
staff_required = roles_required(Role.ADMIN, Role.RECEPTION, Role.DOCTOR)
doctor_required = roles_required(Role.ADMIN, Role.DOCTOR)


def user_clinic(user):
    if user.is_superuser:
        return getattr(user, "clinic", None)
    return user.clinic
