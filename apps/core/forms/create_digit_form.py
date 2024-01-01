from django import forms
from apps.core.models import Digit
from apps.taxonomy.models import Unit


class CreateDigitForm(forms.ModelForm):
    """
    Form for updating an existing digit's details.
    """
    taxonomic_unit = forms.ModelChoiceField(
        queryset=Unit.objects.none(),
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit')

    def __init__(self, *args, **kwargs):
        super(CreateDigitForm, self).__init__(*args, **kwargs)
