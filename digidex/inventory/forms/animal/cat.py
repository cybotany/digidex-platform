from django import forms
from digidex.inventory.models import Pet, Grouping

class CatForm(forms.ModelForm):
    """
    Form for creating a digitizied representation of a Pet.
    """
    grouping = forms.ModelChoiceField(
        queryset=Grouping.objects.none(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'dropdown-field base-input'
        }),
        label="Grouping"
    )
    class Meta:
        model = Pet
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
        super(PetForm, self).__init__(*args, **kwargs)
        
        if user is not None:
            self.fields['grouping'].queryset = Grouping.objects.filter(user=user)
