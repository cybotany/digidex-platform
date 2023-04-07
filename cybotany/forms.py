# forms.py

from django import forms
from .models import Plant, Experiment

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = [
            'user_cea', 'start_date', 'end_date', 'description', 'peer_reviewed_publication'
        ]

    def clean(self):
        cleaned_data = super().clean()
        peer_reviewed_publication = cleaned_data.get("peer_reviewed_publication")

        if peer_reviewed_publication:
            # Add your custom validation logic here, e.g.:
            # if some_field is empty or doesn't meet the requirement:
            #     self.add_error('some_field', 'This field is required for peer-reviewed publications.')

            # Ensure all required fields are properly filled in and meet the NCERA-101 guidelines
            pass

        return cleaned_data


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['image', 'name', 'health_status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plant Name'}),
            'health_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Health Status'}),
        }
