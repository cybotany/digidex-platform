from django import forms
from apps.core.models import Digit


class CreateDigitForm(forms.ModelForm):
    """
    Form for updating an existing digit's details.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'group', 'link', 'taxonomic_unit', 'user')

    def __init__(self, *args, **kwargs):
        super(CreateDigitForm, self).__init__(*args, **kwargs)
