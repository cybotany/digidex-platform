from django import forms
from digidex.journal.models import Entry


class CreateEntryForm(forms.ModelForm):
    """
    Form for creating a new journal entry.
    """

    class Meta:
        model = Entry
        fields = ('watered', 'fertilized', 'cleaned', 'content', 'image')

    def __init__(self, *args, **kwargs):
        super(CreateEntryForm, self).__init__(*args, **kwargs)
