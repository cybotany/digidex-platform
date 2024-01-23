from django import forms
from digit.journal.models import Entry


class CreateJournalEntry(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Entry
        fields = ('content', 'image', 'watered', 'fertilized', 'cleaned')

    def __init__(self, *args, **kwargs):
        super(CreateJournalEntry, self).__init__(*args, **kwargs)
