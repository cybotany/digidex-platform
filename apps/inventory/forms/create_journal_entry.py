from django import forms
from apps.inventory.models import Journal


class CreateJournalEntry(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Journal
        fields = ['entry', 'image']

    def __init__(self, *args, **kwargs):
        self.digit = kwargs.pop('digit', None)
        self.user = kwargs.pop('user', None)
        super(CreateJournalEntry, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Save the form's fields to the associated model.
        """
        journal_entry = super().save(commit=False)
        journal_entry.digit = self.digit
        journal_entry.user = self.user
        if commit:
            journal_entry.save()
        return journal_entry