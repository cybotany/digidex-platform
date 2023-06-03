from django import forms
from ..models import Instrument


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'type', 'description']
