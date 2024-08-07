from django import forms

from inventory.models import InventoryAssetPage, InventoryLink


class InventoryAssetForm(forms.ModelForm):
    taxon_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    species = forms.CharField(
        max_length=255,
        required=False,
        label='Species'
    )
    decouple_nfc_tag = forms.BooleanField(
        required=False,
        label="Decouple NFC TAG"
    )

    class Meta:
        model = InventoryAssetPage
        fields = ['name', 'description', 'species', 'taxon_id']
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
            self.fields['decouple_nfc_tag'].widget.attrs.update(
                {'class': 'w-commerce-commercecheckoutbillingaddresstogglecheckbox'}
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

    def clean_species_name(self):
        return self.cleaned_data['species']

    def clean_taxon_id(self):
        taxon_id = self.cleaned_data['taxon_id']
        if not taxon_id:
            raise forms.ValidationError("You must select a valid species from the suggestions.")
        return taxon_id
