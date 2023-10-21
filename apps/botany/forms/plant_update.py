from django import forms
from apps.botany.models import Plant, PlantImage, PlantWatering, PlantFertilization
from apps.itis.models import TaxonomicUnits


class PlantUpdateForm(forms.ModelForm):
    """
    Form for updating an existing plant's details including uploading an image.
    """
    image = forms.ImageField(required=False)
    watered = forms.BooleanField(required=False)
    fertilized = forms.BooleanField(required=False)
    tsn = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'watered', 'fertilized', 'tsn')

    def __init__(self, *args, **kwargs):
        super(PlantUpdateForm, self).__init__(*args, **kwargs)
        self.fields['tsn'].widget.attrs.update({'id': 'tsnField'})

    def clean(self):
        cleaned_data = super().clean()
        tsn_value = cleaned_data.get('tsn')
        
        if not tsn_value:
            cleaned_data['tsn'] = None
        else:
            try:
                taxonomic_unit = TaxonomicUnits.objects.get(tsn=tsn_value)
                cleaned_data['tsn'] = taxonomic_unit
            except TaxonomicUnits.DoesNotExist:
                raise forms.ValidationError(f"TSN {tsn_value} does not exist!")
        return cleaned_data

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
