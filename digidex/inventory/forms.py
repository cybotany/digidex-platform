from django import forms

from inventory.models import UserInventoryIndex, UserInventoryAsset


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventoryIndex
        fields = ['description']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter a description'
                }
            ),
        }


class UserInventoryAssetForm(forms.ModelForm):
    class Meta:
        model = UserInventoryAsset
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter a name for the asset'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': "Enter the asset's description"
                }
            ),
        }


class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        )
    )
