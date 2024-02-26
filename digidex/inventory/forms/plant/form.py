from digidex.inventory.models import Plant
from ..base import DigitForm

class PlantForm(DigitForm):
    """
    Form for creating a digitizied representation of a Plant.
    """
    class Meta:
        model = Plant

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
