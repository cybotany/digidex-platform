from django import forms

from inventory.models import UserInventoryPage


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventoryPage
        fields = ['description']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'text-field w-input',
                    'placeholder': 'Enter a description'
                }
            )
        }
