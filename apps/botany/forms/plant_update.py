from django import forms
from apps.botany.models import Plant, PlantImage, PlantWatering


class PlantUpdateForm(forms.ModelForm):
    """
    Form for updating an existing plant's details including uploading an image.

    Attributes:
        image (ImageField): Optional image to be uploaded for the plant.
        watered (BooleanField): Whether the plant was watered.
    """

    image = forms.ImageField(required=False)
    watered = forms.BooleanField(required=False)

    class Meta:
        """
        Meta class for the PlantUpdateForm.

        Attributes:
            model (Model): The model class to associate with this form.
            fields (list): Fields to be included in this form.
        """
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'watered')

    def save(self, commit=True):
        """
        Save the form's fields to the associated model.

        Args:
            commit (bool): Whether to commit the changes to the database.

        Returns:
            instance (Model): The model instance updated with form's data.
        """
        instance = super().save(commit)
        image = self.cleaned_data.get('image')
        watered = self.cleaned_data.get('watered')

        if image:
            PlantImage.objects.create(plant=instance, image=image)

        if watered:
            PlantWatering.objects.create(plant=instance, watered=watered)

        return instance
