from django import forms
from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['image', 'name', 'health_status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plant Name'}),
            'health_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Health Status'}),
        }
