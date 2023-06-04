from django import forms
from ..models import TissueCultureChamber


class TissueCultureRegistrationForm(forms.ModelForm):
    class Meta:
        model = TissueCultureChamber
        fields = ('name', 'description', 'column1',)
