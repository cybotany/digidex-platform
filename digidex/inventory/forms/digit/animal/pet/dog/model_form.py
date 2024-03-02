from digidex.inventory.forms import base as inv_forms
from digidex.inventory.models.digit.animal.pet import dog

class PetDogModelForm(inv_forms.AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a pet dog.
    """
    grouping = inv_forms.ModelChoiceField(
        required=True,
        widget=inv_forms.Select(attrs={
            'class': 'dropdown-field base-input'
        }),
        label="Grouping"
    )
    class Meta:
        model = dog.PetDog
        fields = ('name', 'description',)
        widgets = {
            'name': inv_forms.TextInput(attrs={
                'class': 'text-field base-input'
            }),
            'description': inv_forms.Textarea(attrs={
                'class': 'text-field textarea'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PetDogModelForm, self).__init__(*args, **kwargs)
