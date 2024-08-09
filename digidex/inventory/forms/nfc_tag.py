from django import forms

from inventory.models import InventoryAssetPage, NearFieldCommunicationRecord


class NearFieldCommunicationTagForm(forms.ModelForm):

    class Meta:
        model = NearFieldCommunicationRecord
        fields = ['asset']

    def __init__(self, *args, **kwargs):
        user_inventory = kwargs.pop('user_inventory', None)
        super().__init__(*args, **kwargs)
        
        if user_inventory:
            linked_assets = NearFieldCommunicationRecord.objects.filter(asset__isnull=False).values_list('asset_id', flat=True)
            self.fields['asset'].queryset = InventoryAssetPage.objects.child_of(user_inventory).exclude(id__in=linked_assets)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
