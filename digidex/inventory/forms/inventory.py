from django import forms

from inventory.models import TrainerInventoryPage


class TrainerInventoryForm(forms.ModelForm):
    class Meta:
        model = TrainerInventoryPage
        fields = ['description']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'text-field w-input',
                    'placeholder': 'Enter a description'
                }
            )
        }
