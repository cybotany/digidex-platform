from django import forms
from apps.inventory.models import Digit


class CreateDigitForm(forms.ModelForm):
    """
    Form for updating an existing digit's details.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit', 'nfc_link')

    def __init__(self, *args, **kwargs):
        super(CreateDigitForm, self).__init__(*args, **kwargs)
