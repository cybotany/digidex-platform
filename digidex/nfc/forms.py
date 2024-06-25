from django import forms

class DigitalObjectJournalEntryForm(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Provide an image of the object',
            }
        )
    )
    caption = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Provide a caption for the image'
            }
        )
    )
    note = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'textarea base-input',
                'placeholder': 'Provide a note for the journal entry (optional).'
            }
        ),
        required=False
    )
