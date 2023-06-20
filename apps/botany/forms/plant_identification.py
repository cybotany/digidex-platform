from django import forms


class PlantIdentificationForm(forms.Form):
    images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))

    def clean_images(self):
        images = self.files.getlist('images')
        # Validate images if necessary, e.g. check if there's at least one image
        if not images:
            raise forms.ValidationError('You must upload at least one image.')
        return images
