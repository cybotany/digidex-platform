from django import forms
from digidex.inventory.models import Digit
from digidex.taxonomy.models import Unit


class DigitForm(forms.ModelForm):
    """
    Form for creating a digit.
    """

    class Meta:
        model = Digit
        fields = ('name', 'description', 'taxonomic_unit',)
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'nameField',
                'class': 'text-field base-input'
            }),
            'description': forms.Textarea(attrs={
                'id': 'descriptionField',
                'class': 'text-field textarea'
            }),
            'taxonomic_unit': forms.Select(attrs={
                'id': 'tsnField',
                'class': 'text-field base-select',
            }),

        }

    def __init__(self, *args, **kwargs):
        super(DigitForm, self).__init__(*args, **kwargs)
        # Initialize taxonomic_unit field as empty
        self.fields['taxonomic_unit'].queryset = Digit.objects.none()

    def clean_taxonomic_unit(self):
        tsn = self.cleaned_data.get('taxonomic_unit')
        if tsn:
            try:
                taxonomic_unit = Unit.objects.get(tsn=tsn)
                return taxonomic_unit
            except Unit.DoesNotExist:
                raise forms.ValidationError('Invalid Taxonomic Serial Number')
        return None
