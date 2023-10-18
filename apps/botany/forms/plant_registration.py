from django import forms
from apps.botany.models import Plant, PlantImage
from apps.itis.models import TaxonomicUnits


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.

    This form allows users to register a new plant with attributes
    such as name, label, common names, and description.
    Users can also upload an image of the plant.
    """

    nfc_tag = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    tsn = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'nfc_tag', 'tsn')

    def __init__(self, *args, **kwargs):
            """
            Initialize the form.

            Pop the user, nfc_tag, and tsn from kwargs.
            """
            self.user = kwargs.pop('user', None)
            self.nfc_tag = kwargs.pop('nfc_tag', None)
            super().__init__(*args, **kwargs)

            if self.nfc_tag:
                self.fields['nfc_tag'].initial = self.nfc_tag

            # Set the ID for the tsn field
            self.fields['tsn'].widget.attrs.update({'id': 'tsnField'})

    def clean(self):
        cleaned_data = super().clean()
        tsn_value = cleaned_data.get('tsn')
        if tsn_value:
            try:
                taxonomic_unit = TaxonomicUnits.objects.get(tsn=tsn_value)
                cleaned_data['tsn'] = taxonomic_unit
            except TaxonomicUnits.DoesNotExist:
                raise forms.ValidationError(f"TSN {tsn_value} does not exist!")
        return cleaned_data

    def save(self, commit=True):
        """
        Save the form.

        Associates the plant with the owner (user) and saves the uploaded image.
        Also ensures that the TSN value is converted to a TaxonomicUnits instance.
        """
        plant = super().save(commit=False)
        plant.user = self.user

        if commit:
            plant.save()
            image = self.cleaned_data.get('image')
            if image:
                PlantImage.objects.create(plant=plant, image=image)

        return plant
