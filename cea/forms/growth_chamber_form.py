from django import forms
from plants.models import GrowthChamber


class GrowthChamberForm(forms.ModelForm):
    class Meta:
        model = GrowthChamber
        fields = ('name', 'description', 'location', 'measurement_system', 'chamber_width', 'chamber_height', 'chamber_length', 'sensors', 'instruments')
