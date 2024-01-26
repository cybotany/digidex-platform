from django import forms
from digidex.inventory.models import Journal


class JournalEntryForm(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Journal
        fields = ('content', 'image', 'watered', 'fertilized', 'cleaned')

    def __init__(self, *args, **kwargs):
        super(JournalEntryForm, self).__init__(*args, **kwargs)
