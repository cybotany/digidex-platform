from digidex.inventory.forms.digitized import _base_forms
from digidex.inventory.models.digitized import group

class ItemizedDigitGroupModelForm(_base_forms._AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a grouping of digitized entites.
    """
    class Meta:
        model = group.ItemizedDigitGroup
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(ItemizedDigitGroupModelForm, self).__init__(*args, **kwargs)
