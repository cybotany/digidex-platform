from django import forms

from inventorytags.models import InventoryLink


class AssociateNtagForm(forms.ModelForm):
    class Meta:
        model = InventoryLink
        fields = ['asset']

    def __init__(self, *args, **kwargs):
        user_inventory = kwargs.pop('user_inventory', None)
        super().__init__(*args, **kwargs)
        if user_inventory:
            from inventory.models import InventoryAssetPage
            self.fields['asset'].queryset = InventoryAssetPage.objects.child_of(user_inventory)
            self.fields['asset'].widget.attrs.update({'class': 'custom-dropdown-class'})


class DeletionConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        )
    )
