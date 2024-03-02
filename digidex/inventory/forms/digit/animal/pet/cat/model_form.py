from django import forms
from digidex.inventory.models.digit.animal.pet import cat

class PetCatModelForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    grouping = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'dropdown-field base-input'
        }),
        label="Grouping"
    )
    class Meta:
        model = cat.PetCat
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
        user = kwargs.pop('user', None)
        super(PetCatModelForm, self).__init__(*args, **kwargs)
