from django import forms
from ..models import Plant

class PlantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('name')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        plant = super().save(commit=False)
        plant.owner = self.user
        if commit:
            plant.save()
        return plant
