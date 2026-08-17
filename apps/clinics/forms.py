from django import forms
from django.contrib.auth.password_validation import validate_password

from apps.accounts.models import Role, StaffUser
from apps.clinics.models import Clinic, Doctor, Room, TokenScope, WorkingHours


class ClinicSetupForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = [
            "name",
            "slug",
            "token_scope",
            "average_consult_minutes",
            "notify_when_ahead",
            "notifications_enabled",
            "appointment_priority_grace_minutes",
            "timezone",
        ]
        widgets = {
            "token_scope": forms.Select(choices=TokenScope.choices),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["display_name", "specialization", "is_active", "average_consult_minutes"]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "doctor"]

    def __init__(self, *args, clinic: Clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = Doctor.objects.filter(clinic=clinic)
        self.fields["doctor"].required = False


class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ["doctor", "weekday", "start_time", "end_time", "slot_minutes"]

    def __init__(self, *args, clinic: Clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = Doctor.objects.filter(clinic=clinic)
        self.fields["doctor"].required = False
        self.fields["weekday"].widget = forms.Select(
            choices=[(i, d) for i, d in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])]
        )


class StaffInviteForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=False)
    role = forms.ChoiceField(choices=Role.choices)
    password = forms.CharField(widget=forms.PasswordInput, min_length=12)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), required=False)

    def __init__(self, *args, clinic: Clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.clinic = clinic
        self.fields["doctor"].queryset = Doctor.objects.filter(clinic=clinic)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if StaffUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        return password

    def save(self) -> StaffUser:
        user = StaffUser(
            username=self.cleaned_data["username"],
            email=self.cleaned_data.get("email") or "",
            role=self.cleaned_data["role"],
            clinic=self.clinic,
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
        doctor = self.cleaned_data.get("doctor")
        if user.role == Role.DOCTOR and doctor:
            doctor.staff_user = user
            doctor.save(update_fields=["staff_user"])
        return user
