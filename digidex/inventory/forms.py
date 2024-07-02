from django import forms
from django.core.exceptions import ValidationError

class InventoryForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the inventory'
            }
        ),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': 'Provide a detailed description of the object'
            }
        ),
        required=False
    )

    def clean_name(self):
        title = self.cleaned_data['title']
        forbidden_keywords = ['add', 'update', 'delete', 'admin']
        if any(keyword in title.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The name cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')
        return title


class DeleteInventoryForm(forms.Form):
    delete = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        ),
        required=True
    )


class InventoryAssetForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the title of the digitized object'
            }
        ),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': 'Provide a detailed description of the object'
            }
        ),
        required=False
    )


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
