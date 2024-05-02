from django import forms
from .models import DigitizedObject

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description']  # Specify the fields you want to include in the form

    def __init__(self, *args, **kwargs):
        super(DigitizedObjectForm, self).__init__(*args, **kwargs)
        # Custom initialization can go here, for example, setting custom widgets
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control rich-text'})
