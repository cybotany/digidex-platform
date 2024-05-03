from django import forms

from digitization.models import DigitizedObject

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-field base-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-field textarea'
            }),
        }

    def clean(self):
       pass