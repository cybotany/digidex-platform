from django import forms
from apps.cea.models import TissueCultureChamber


class TissueCultureRegistrationForm(forms.ModelForm):
    class Meta:
        model = TissueCultureChamber
        fields = ('name', 'description', 'column1',)
