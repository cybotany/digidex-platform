from django import forms
from django.core.exceptions import ValidationError

from inventory.models import Inventory, Asset


class InventoryForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter a name'
            }
        ),
        required=True
    )
    search_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': '(Optional) Provide a description'
            }
        ),
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['title']
        forbidden_keywords = ['add', 'update', 'delete', 'remove', 'edit', 'create', 'destroy', 'new', 'old', 'current', 'previous', 'next', 'last', 'first', 'all', 'any', 'some',]
        if any(keyword in name.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The name cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')
        return name

    class Meta:
        model = Inventory
        fields = ['title', 'search_description']


class AssetForm(forms.ModelForm):
    pass
