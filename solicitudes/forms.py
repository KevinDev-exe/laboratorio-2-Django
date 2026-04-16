from django import forms
from .models import Solicitud


class solicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '_all_'