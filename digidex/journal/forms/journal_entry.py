from django import forms
from django.core.exceptions import ValidationError
from digidex.journal.models import Entry

class JournalEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'text-field textarea base-input'
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
                #'class': 'base-file-upload-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(JournalEntry, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')

        # Check if both fields are left blank
        if not content and not image:
            raise ValidationError('You must fill out at least one of the fields: Content or Image.')

        return cleaned_data
