from digidex.inventory.forms import base as inv_forms
from digidex.inventory.models.group import base as inv_group

class ItemizedDigitGroupModelForm(inv_forms.AbstractInventoryModelForm):
    """
    Form for creating a digitizied representation of a grouping of digitized entites.
    """
    class Meta:
        model = inv_group.ItemizedDigitGroup
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(ItemizedDigitGroupModelForm, self).__init__(*args, **kwargs)
