from digidex.inventory.forms.digitized import _base_forms
from digidex.inventory.models.digitized import pet

class _DigitizedPetModelForm(_base_forms._AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = None
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(_DigitizedPetModelForm, self).__init__(*args, **kwargs)


class DigitiziedPetDogModelForm(_base_forms.AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a pet dog.
    """
    class Meta:
        model = pet.DigitizedPetDog
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
        super(DigitiziedPetDogModelForm, self).__init__(*args, **kwargs)


class PetCatModelForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = pet.PetCat
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
