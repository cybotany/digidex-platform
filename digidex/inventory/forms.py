from django import forms

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


class AssociateNtagForm(forms.ModelForm):
    class Meta:
        model = InventoryLink
        fields = ['asset', 'url']

    def __init__(self, *args, **kwargs):
        user_inventory = kwargs.pop('user_inventory', None)
        super().__init__(*args, **kwargs)
        if user_inventory:
            from inventory.models import InventoryAssetPage
            self.fields['asset'].queryset = InventoryAssetPage.objects.child_of(user_inventory)
            self.fields['asset'].widget.attrs.update({'class': 'custom-dropdown-class'})
        self.fields['url'].widget.attrs.update({'class': 'text-field w-input'})


class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'w-radio',
            }
        )
    )
