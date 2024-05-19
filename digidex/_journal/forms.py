from django import forms

from _journal.models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ('image', 'caption',)
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
            )
        }
