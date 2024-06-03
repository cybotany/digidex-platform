from django import forms

from base.forms import AssetDeletionCheckbox

class DigitalObjectForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the digitized object'
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

class InventoryDigitDeletionForm(AssetDeletionCheckbox):
    pass
