from django import forms
from digidex.inventory.models import Journal


class CreateJournalEntry(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Journal
        fields = ('content', 'image', 'watered', 'fertilized', 'cleaned')

    def __init__(self, *args, **kwargs):
        super(CreateJournalEntry, self).__init__(*args, **kwargs)
