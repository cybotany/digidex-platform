from django import forms

from base.forms import AssetDeletionCheckbox

class DigitalObjectForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the digitized object'
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

class DigitalObjectDeletionForm(AssetDeletionCheckbox):
    pass



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
