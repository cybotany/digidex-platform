from digidex.inventory.forms import _base
from digidex.inventory.models.digit import group

class ItemizedDigitGroupModelForm(_base._AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a grouping of digitized entites.
    """
    class Meta:
        model = group.ItemizedDigitGroup
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(ItemizedDigitGroupModelForm, self).__init__(*args, **kwargs)
