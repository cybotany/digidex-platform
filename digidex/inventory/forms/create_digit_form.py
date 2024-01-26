from django import forms
from digidex.inventory.models import Digit


class CreateDigitForm(forms.ModelForm):
    """
    Form for creating a digit.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit',)

    def __init__(self, *args, **kwargs):
        super(CreateDigitForm, self).__init__(*args, **kwargs)
