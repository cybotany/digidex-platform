from django import forms

from inventory.models import UserInventory, InventoryCategory, InventoryAsset


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter a name for the inventory'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': "Enter the inventory's description"
                }
            ),
        }



class InventoryCategoryForm(forms.ModelForm):
    class Meta:
        model = InventoryCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter a name for the category'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': "Enter the category's description"
                }
            ),
        }



class InventoryAssetForm(forms.ModelForm):
    class Meta:
        model = InventoryAsset
        fields = ['name', 'category','description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter a name for the asset'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'select-field base-input',
                    'placeholder': 'Select a category'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': "Enter the asset's description"
                }
            ),
        }


    def __init__(self, *args, **kwargs):
        inventory = kwargs.pop('inventory', None)
        super().__init__(*args, **kwargs)
        if inventory:
            self.fields['category'].queryset = InventoryCategory.objects.filter(inventory=inventory)


class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        )
    )
