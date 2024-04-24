from django import forms

from inventory import forms


class UserDigitForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Plant.
    """
    class Meta:
        model = plant.DigitizedHousePlant
        fields = ('name', 'description', 'taxon',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-field base-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-field textarea'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(_DigitizedPlantForm, self).__init__(*args, **kwargs)
