from django import forms
from digit.inventory.models import Digit


class ModifyDigitForm(forms.ModelForm):
    """
    Form for modifying an existing digit's details, including the thumbnail image.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit', 'thumbnail')

    def __init__(self, *args, **kwargs):
        super(ModifyDigitForm, self).__init__(*args, **kwargs)
        # Additional form customization (if needed) can be added here
