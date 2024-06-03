from django import forms

from base.forms import AssetDeletionCheckbox
from inventory.models import InventoryCategoryPage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = InventoryCategoryPage
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

class CategoryDeletionForm(AssetDeletionCheckbox):
    pass
