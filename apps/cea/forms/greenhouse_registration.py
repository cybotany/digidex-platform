from django import forms
from apps.cea.models import Greenhouse


class GreenhouseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ('name', 'description', 'location',)
