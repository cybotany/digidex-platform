from django import forms
from digit.inventory.models import Digit


class DigitForm(forms.ModelForm):
    """
    Form for creating or modifying an existing digit's details.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit',)

    def __init__(self, *args, **kwargs):
        super(DigitForm, self).__init__(*args, **kwargs)
