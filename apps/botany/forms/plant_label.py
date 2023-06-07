from django import forms
from ..models import Label

class PlantLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)
