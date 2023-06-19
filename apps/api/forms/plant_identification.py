from django import forms


class PlantIdentificationForm(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    location = forms.CharField(max_length=255, required=False)  # location can be optional

    def clean_images(self):
        images = self.files.getlist('images')
        # Validate images if necessary, e.g. check if there's at least one image
        if not images:
            raise forms.ValidationError('You must upload at least one image.')
        return images

    def identify_plant(self):
        images = self.cleaned_data.get('images')
        location = self.cleaned_data.get('location')
        # Call the plant identification API
        # The exact details would depend on the API
        results = some_api_call(images, location)
        return results
