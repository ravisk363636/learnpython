from django import forms

from apps.clinics.models import Doctor
from apps.queues.models import Token


class IssueTokenForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none())
    patient_name = forms.CharField(max_length=120)
    patient_phone = forms.CharField(max_length=32, required=False)
    patient_email = forms.EmailField(required=False)

    def __init__(self, *args, clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = Doctor.objects.filter(clinic=clinic, is_active=True)


class ReorderForm(forms.Form):
    token = forms.ModelChoiceField(queryset=Token.objects.none(), widget=forms.HiddenInput)
    new_sort_order = forms.IntegerField(min_value=0)

    def __init__(self, *args, clinic, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["token"].queryset = Token.objects.filter(clinic=clinic)
