from django import forms
from digidex.journal.models import Entry


class JournalEntryForm(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Entry
        fields = ('content', 'image')

    def __init__(self, *args, **kwargs):
        super(JournalEntryForm, self).__init__(*args, **kwargs)
