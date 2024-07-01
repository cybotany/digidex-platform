from django import forms
from django.apps import apps


class NearFieldCommunicationAssetForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the title of the digitized object'
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
    inventory = forms.ModelChoiceField(
        queryset=None,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'dropdown'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            InventoryPage = apps.get_model('inventory', 'InventoryPage')
            self.fields['inventory'].queryset = InventoryPage.objects.filter(owner=user)
