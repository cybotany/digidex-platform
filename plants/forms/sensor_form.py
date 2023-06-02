from django import forms
from plants.models import Sensor


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'type', 'description', 'min_value', 'max_value', 'value_unit']
