from django import forms

from wagtail.images import get_image_model
from wagtail.admin.forms.models import WagtailAdminModelForm

from .models import Note, NoteImageGallery


DigiDexImageModel = get_image_model()

class JournalEntryForm(WagtailAdminModelForm):
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = Note
        fields = ['entry', 'images']

    def save(self, commit=True):
        note = super().save(commit=False)
        if commit:
            note.save()
            images = self.files.getlist('images')
            for image_file in images:
                image = DigiDexImageModel(
                    title=image_file.name,
                    file=image_file,
                    collection=note.collection
                )
                image.save()
                NoteImageGallery.objects.create(note=note, image=image)
        return note
