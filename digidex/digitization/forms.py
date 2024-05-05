from django import forms

from digitization.models import DigitizedObject, DigitizedObjectImage

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea'
                }
            ),
        }


class DigitizedObjectImageForm(forms.ModelForm):
    class Meta:
        model = DigitizedObjectImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'text-field base-input'}
            ),
            'caption': forms.TextInput(
                attrs={'class': 'text-field base-input'}
            ),
        }
