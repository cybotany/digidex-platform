from django import forms


class PlantIdentificationForm(forms.Form):
    image = forms.FileField(widget=forms.FileInput())

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('You must upload an image.')
        return image
