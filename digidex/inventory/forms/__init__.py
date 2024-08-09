from django.forms import Form, BooleanField, CheckboxInput

from .asset import InventoryAssetForm


class DeletionConfirmationForm(Form):
    confirmation = BooleanField(
        required=True,
        widget=CheckboxInput(
            attrs={
                'class': 'w-radio',
            }
        )
    )
