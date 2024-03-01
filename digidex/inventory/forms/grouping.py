from django import forms

from digidex.inventory.models import grouping as inventory_group

class InventoryGroupingForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a grouping of digitized entites.
    """
    class Meta:
        model = inventory_group.Grouping
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-field base-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-field textarea'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(InventoryGroupingForm, self).__init__(*args, **kwargs)
