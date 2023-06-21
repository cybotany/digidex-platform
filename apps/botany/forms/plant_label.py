from django import forms
from apps.botany.models import Label


class PlantLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)
