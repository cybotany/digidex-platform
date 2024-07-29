from django import forms


class UserInventoryForm(forms.Form):
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter a description'
            }
        )
    )

class UserInventoryAssetForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter a name for the asset'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': "Enter the asset's description"
            }
        )
    )

class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        )
    )
