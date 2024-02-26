from django import forms
from digidex.inventory.models import Pet

class PetForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = Pet
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
        super(PetForm, self).__init__(*args, **kwargs)
