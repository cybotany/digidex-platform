from django import forms
from digit.journal.models import Entry


class JournalEntryForm(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Entry
        fields = ('content', 'image', 'watered', 'fertilized', 'cleaned')

    def __init__(self, *args, **kwargs):
        super(JournalEntryForm, self).__init__(*args, **kwargs)
