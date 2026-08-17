from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit


class StaffLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_active:
            raise self.get_invalid_login_error()


@method_decorator(ratelimit(key="ip", rate="10/m", method="POST", block=True), name="dispatch")
class StaffLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = StaffLoginForm
    redirect_authenticated_user = True


class StaffLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")
