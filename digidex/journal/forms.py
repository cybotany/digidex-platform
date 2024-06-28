from django import forms
from django.forms.widgets import ClearableFileInput

from wagtail.images import get_image_model

from .models import JournalEntry


DigiDexImageModel = get_image_model()

class JournalEntryForm(forms.ModelForm):
    image = forms.ImageField(
        widget=ClearableFileInput(),
        required=False
    )

    class Meta:
        model = JournalEntry
        fields = ['entry', 'image']

    def __init__(self, *args, **kwargs):
        self.collection = kwargs.pop('collection', None)
        self.content_object = kwargs.pop('content_object', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.collection:
            instance.image.collection = self.collection
        if self.content_object:
            instance.content_object = self.content_object
        if commit:
            instance.save()
            self.save_m2m()
        return instance
