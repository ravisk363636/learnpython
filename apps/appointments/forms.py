from django import forms

from apps.clinics.models import Doctor


class BookAppointmentForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none())
    start_at = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"])
    patient_name = forms.CharField(max_length=120)
    patient_phone = forms.CharField(max_length=32, required=False)
    patient_email = forms.EmailField(required=False)

    def __init__(self, *args, clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = Doctor.objects.filter(clinic=clinic, is_active=True)
        self.fields["start_at"].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})
