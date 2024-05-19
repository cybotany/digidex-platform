from django import forms

from digitization.models import UserDigit


class UserDigitForm(forms.ModelForm):
    class Meta:
        model = UserDigit
        fields = ('name', 'description',)
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
            )
        }
