from django.apps import apps
from django import forms


class UserInventoryForm(forms.ModelForm):
    class Meta:
        UserInventory = apps.get_model('inventory', 'UserInventory')
        model = UserInventory
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the inventory'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            )
        }


class UserDigitForm(forms.ModelForm):
    class Meta:
        UserDigit = apps.get_model('inventory', 'UserDigit')
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


class JournalEntryForm(forms.ModelForm):
    class Meta:
        JournalEntry = apps.get_model('inventory', 'JournalEntry')
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
