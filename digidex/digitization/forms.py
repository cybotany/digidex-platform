from django import forms
from .models import DigitizedObject

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(DigitizedObjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control rich-text'})
