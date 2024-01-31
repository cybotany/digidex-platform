from django import forms
from digidex.inventory.models import Digit


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
            'taxonomic_unit': forms.TextInput(attrs={
                'id': 'tsnField',
                'class': 'text-field base-input',
            }),

        }

    def __init__(self, *args, **kwargs):
        super(DigitForm, self).__init__(*args, **kwargs)
        # Initialize taxonomic_unit field as empty
        self.fields['taxonomic_unit'].queryset = Digit.objects.none()
