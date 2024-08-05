from django import forms

from inventory.models import UserInventoryPage, InventoryAssetPage, InventoryLink


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventoryPage
        fields = ['description']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'text-field w-input',
                    'placeholder': 'Enter a description'
                }
            )
        }


class InventoryAssetForm(forms.ModelForm):
    class Meta:
        model = InventoryAssetPage
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field w-input',
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


class NearFieldCommunicationLinkedTagForm(forms.ModelForm):
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
