from django import forms
from digidex.inventory.models import Grouping

class GroupingForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a grouping of digitized entites.
    """
    class Meta:
        model = Grouping
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
        super(GroupingForm, self).__init__(*args, **kwargs)
