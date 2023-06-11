from django import forms
from ..models import Plant


class PlantImageForm(forms.ModelForm):
    class Meta:
            model = Plant
            fields = ('image')
