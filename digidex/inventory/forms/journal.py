from django import forms

from base.forms import AssetDeletionCheckbox
from inventory.models.journal import JournalEntry


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ('image', 'caption', 'note',)
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
            'note': forms.Textarea(
                attrs={
                    'class': 'textarea base-input',
                    'placeholder': 'Provide a note for the journal entry (optional).'
                }
            )
        }

class InventoryDigitDeletionForm(AssetDeletionCheckbox):
    pass
