from django import forms

from inventory.models import UserInventory


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventory
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the inventory'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            )
        }
