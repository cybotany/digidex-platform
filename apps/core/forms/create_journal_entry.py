from django import forms
from apps.core.models import Journal


class CreateJournalEntry(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Journal
        fields = ['entry', 'image']

    def __init__(self, *args, **kwargs):
        super(CreateJournalEntry, self).__init__(*args, **kwargs)

        # Initialize form fields here if needed, for example:
        self.fields['image'].required = False
