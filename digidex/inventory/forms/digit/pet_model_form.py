from digidex.inventory.forms import _base
from digidex.inventory.models.digit import pet

class _DigitizedPetModelForm(_base._AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = None
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(_DigitizedPetModelForm, self).__init__(*args, **kwargs)


class DigitiziedPetDogModelForm(_base.AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a pet dog.
    """
    class Meta:
        model = pet.DigitizedPetDog
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DigitiziedPetDogModelForm, self).__init__(*args, **kwargs)


class DigitiziedPetCatModelForm(_base.AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = pet.DigitizedPetCat
        fields = ('name', 'description', 'taxon',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DigitiziedPetCatModelForm, self).__init__(*args, **kwargs)
