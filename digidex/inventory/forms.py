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
    decouple_nfc_tag = forms.BooleanField(
        required=False,
        label="Decouple NFC TAG"
    )

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'linked_tag'):
            self.fields['decouple_nfc_tag'] = forms.BooleanField(
                required=False,
                label="Decouple NFC TAG"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'decouple_nfc_tag' in self.cleaned_data and self.cleaned_data['decouple_nfc_tag']:
            try:
                link = instance.linked_tag
                link.asset = None
                link.save()
            except InventoryLink.DoesNotExist:
                pass

        if commit:
            instance.save()
        return instance


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
            linked_assets = InventoryLink.objects.values_list('asset_id', flat=True)
            self.fields['asset'].queryset = InventoryAssetPage.objects.child_of(user_inventory).exclude(id__in=linked_assets)
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
