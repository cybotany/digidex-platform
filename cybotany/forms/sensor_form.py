from django import forms
from cybotany.models import Sensor


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'type', 'description', 'min_value', 'max_value', 'value_unit']
