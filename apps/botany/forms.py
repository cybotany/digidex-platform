from django import forms
from apps.botany.models import Plant, PlantImage, PlantWatering, PlantFertilization


class PlantForm(forms.ModelForm):
    """
    Form for updating an existing plant's details.
    """
    image = forms.ImageField(
        required=False
    )
    watered = forms.BooleanField(
        required=False
    )
    fertilized = forms.BooleanField(
        required=False
    )

    class Meta:
        model = Plant
        fields = ('quantity', 'image', 'watered', 'fertilized')

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Save the form's fields to the associated model.
        """
        plant = super().save(commit)

        image = self.cleaned_data.get('image')
        if image:
            PlantImage.objects.create(plant=plant, image=image)
        
        watered = self.cleaned_data.get('watered')
        if watered:
            PlantWatering.objects.create(plant=plant, watered=watered)

        fertilized = self.cleaned_data.get('fertilized')
        if fertilized:
            PlantFertilization.objects.create(plant=plant, fertilized=fertilized)

        return plant
