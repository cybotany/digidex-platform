from django import forms
from wagtail.admin.rich_text import DraftailRichTextArea

from inventory.models import InventoryLink


class UserInventoryForm(forms.Form):
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field w-input',
                'placeholder': 'Enter a description'
            }
        )
    )

class InventoryAssetForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field w-input',
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
    body = forms.CharField(
        widget=DraftailRichTextArea(features=None)
    )


class AssociateNtagForm(forms.ModelForm):
    release = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'w-radio',
            }
        )
    )

    class Meta:
        model = InventoryLink
        fields = ['asset']

    def __init__(self, *args, **kwargs):
        user_inventory = kwargs.pop('user_inventory', None)
        super().__init__(*args, **kwargs)
        
        if user_inventory:
            from inventory.models import InventoryAssetPage
            self.fields['asset'].queryset = InventoryAssetPage.objects.child_of(user_inventory)
            # self.fields['asset'].widget.attrs.update({'class': 'custom-dropdown-class'})


class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'w-radio',
            }
        )
    )
