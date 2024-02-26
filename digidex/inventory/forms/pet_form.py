from digidex.inventory.models import Pet
from .digit_form import DigitForm

class PetForm(DigitForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    class Meta:
        model = Pet

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
