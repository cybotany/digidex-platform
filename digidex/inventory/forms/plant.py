from django import forms
from digidex.inventory.models import Plant

class PlantForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Plant.
    """
    class Meta:
        model = Plant
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
        super(PlantForm, self).__init__(*args, **kwargs)
