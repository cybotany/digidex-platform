from django import forms

from base.forms import AssetDeletionCheckbox
from inventory.models import DigitalObjectPage, InventoryCategoryPage


class DigitalObjectForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=InventoryCategoryPage.objects.none(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'select-field base-input',
                'placeholder': 'Select a category'
            }
        )
    )

    class Meta:
        model = DigitalObjectPage
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the digitized object'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DigitalObjectForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = InventoryCategoryPage.objects.filter(user=user)


class InventoryDigitDeletionForm(AssetDeletionCheckbox):
    pass
