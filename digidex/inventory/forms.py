from django import forms

from inventory.models import UserInventory, InventoryCategory, InventoryAsset


class UserInventoryForm(forms.ModelForm):
    class Meta:
        model = UserInventory
        fields = ['name', 'description']


class InventoryCategoryForm(forms.ModelForm):
    class Meta:
        model = InventoryCategory
        fields = ['name', 'description']


class InventoryAssetForm(forms.ModelForm):
    class Meta:
        model = InventoryAsset
        fields = ['name', 'category','description']

    def __init__(self, *args, **kwargs):
        inventory = kwargs.pop('inventory', None)
        super().__init__(*args, **kwargs)
        if inventory:
            self.fields['category'].queryset = InventoryCategory.objects.filter(inventory=inventory)
