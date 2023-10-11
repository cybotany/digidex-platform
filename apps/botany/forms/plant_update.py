from django import forms
from apps.botany.models import Plant, PlantImage, PlantWatering, PlantFertilization


class PlantUpdateForm(forms.ModelForm):
    """
    Form for updating an existing plant's details including uploading an image.

    Attributes:
        image (ImageField): Optional image to be uploaded for the plant.
        watered (BooleanField): Whether the plant was watered.
        fertilized (BooleanField): Whether the plant was fertilized.
    """

    image = forms.ImageField(required=False)
    watered = forms.BooleanField(required=False)
    fertilized = forms.BooleanField(required=False)

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'watered', 'fertilized', 'tsn')

    def save(self, commit=True):
        """
        Save the form's fields to the associated model.
        """
        plant = super().save(commit)
        image = self.cleaned_data.get('image')
        watered = self.cleaned_data.get('watered')
        fertilized = self.cleaned_data.get('fertilized')

        if image:
            PlantImage.objects.create(plant=plant, image=image)

        if watered:
            PlantWatering.objects.create(plant=plant, watered=watered)

        if fertilized:
            PlantFertilization.objects.create(plant=plant, fertilized=fertilized)

        return plant
