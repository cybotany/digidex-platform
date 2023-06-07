from django import forms
from ..models import GrowthChamber


class GrowthChamberRegistrationForm(forms.ModelForm):
    class Meta:
        model = GrowthChamber
        fields = ('name', 'description', 'measurement_system', 'chamber_width', 'chamber_height', 'chamber_length',)
