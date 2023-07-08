from django import forms
from apps.botany.models import GrowingFertilizer


class GrowingFertilizerForm(forms.ModelForm):
    class Meta:
        model = GrowingFertilizer
        fields = ['name', 'description', 'nitrogen', 'phosphorus', 'potassium']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)
