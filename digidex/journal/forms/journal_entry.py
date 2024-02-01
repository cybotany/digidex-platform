from django import forms
from digidex.journal.models import Entry


class JournalEntry(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Entry
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'text-field textarea base-input'
            }),
            #'image': forms.FileInput(attrs={
            #    'accept': 'image/jpeg, image/png',
            #    'class': 'base-file-upload-input',
            #}),
        }

    def __init__(self, *args, **kwargs):
        super(JournalEntry, self).__init__(*args, **kwargs)
