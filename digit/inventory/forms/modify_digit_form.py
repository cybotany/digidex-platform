from django import forms
from digit.inventory.models import Digit


class ModifyDigitForm(forms.ModelForm):
    """
    Form for modifying an existing digit's details.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit',)

    def __init__(self, *args, **kwargs):
        super(ModifyDigitForm, self).__init__(*args, **kwargs)
