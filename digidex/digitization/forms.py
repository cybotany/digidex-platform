from django import forms
from django.forms import inlineformset_factory

from digitization.models import DigitizedObject, DigitizedObjectImage

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description']

DigitizedObjectImageFormSet = inlineformset_factory(
    DigitizedObject,
    DigitizedObjectImage,
    fields=('image', 'caption'),
    extra=1,
    can_delete=True
)
