class ClinicIsolationMiddleware:
    """Attach the staff member's clinic to the request. Superusers may have none."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.clinic = None
        user = getattr(request, "user", None)
        if user is not None and user.is_authenticated:
            request.clinic = getattr(user, "clinic", None)
        return self.get_response(request)
