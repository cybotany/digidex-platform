from django import forms
from apps.botany.models import Plant, PlantImage, PlantWatering, PlantFertilization, Group


class PlantUpdateForm(forms.ModelForm):
    """
    Form for updating an existing plant's details.
    """
    # Optional field to upload a new image for the plant
    image = forms.ImageField(
        required=False
    )
    # Optional field to record a watering event
    watered = forms.BooleanField(
        required=False
    )
    # Optional field to record a fertilization event
    fertilized = forms.BooleanField(
        required=False
    )
    # Group field is populated dynamically in the __init__ method
    group = forms.ModelChoiceField(
        queryset=Group.objects.none(),
        required=False,
        widget=forms.Select(attrs={'id': 'groupField'})
    )

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'watered', 'fertilized', 'group')

    def __init__(self, *args, **kwargs):
        super(PlantUpdateForm, self).__init__(*args, **kwargs)
        user = kwargs['instance'].user
        self.fields['group'].queryset = Group.objects.filter(user=user)

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
