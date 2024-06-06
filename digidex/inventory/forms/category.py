from django import forms
from django.core.exceptions import ValidationError

from base.forms import AssetDeletionCheckbox


class InventoryCategoryForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the inventory'
            }
        ),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': 'Provide a detailed description of the object'
            }
        ),
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_keywords = ['add', 'update', 'delete', 'admin']
        if any(keyword in name.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The name cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')
        return name


class InventoryCategoryDeletionForm(AssetDeletionCheckbox):
    pass
