from django import forms

from wagtail.images import get_image_model


DigiDexImageModel = get_image_model()

class JournalEntryForm(forms.Form):
    entry = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'textarea base-input',
                'placeholder': 'Provide a entry for the journal entry (optional).'
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Provide an image of the object',
            }
        ),
        required=False
    )
    alt_text = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Provide a caption for the image'
            }
        ),
        required=False
    )
    caption = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Provide a caption for the image'
            }
        ),
        required=False
    )
