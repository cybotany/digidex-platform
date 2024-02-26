from django import forms

class DigitForm(forms.ModelForm):
    """
    Abstract form for creating a digitizied representation of an object.
    """
    class Meta:
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
        super(DigitForm, self).__init__(*args, **kwargs)
