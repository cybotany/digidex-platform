from django import forms

from digitization.models import DigitizedObject, DigitizedObjectImage

class DigitizedObjectForm(forms.ModelForm):
    class Meta:
        model = DigitizedObject
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the digitized object'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            ),
        }


class DigitizedObjectImageForm(forms.ModelForm):
    class Meta:
        model = DigitizedObjectImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'placeholder': 'Provide an image of the object',
                }
            ),
            'caption': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Provide a caption for the image'
                }
            ),
        }
