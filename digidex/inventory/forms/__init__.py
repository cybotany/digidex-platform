from django.forms import Form, BooleanField, CheckboxInput

from .asset import InventoryAssetForm
from .nfc_tag import NearFieldCommunicationTagForm


class DeletionConfirmationForm(Form):
    confirmation = BooleanField(
        required=True,
        widget=CheckboxInput(
            attrs={
                'class': 'w-radio',
            }
        )
    )
