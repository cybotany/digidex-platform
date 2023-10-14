from django import forms
from apps.botany.models import Plant, PlantImage


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.

    This form allows users to register a new plant with attributes
    such as name, label, common names, and description.
    Users can also upload an image of the plant.
    """

    nfc_tag = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    tsn = forms.IntegerField(required=False)

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

    def save(self, commit=True):
        """
        Save the form.

        Associates the plant with the owner (user) and saves the uploaded image.
        """
        plant = super().save(commit=False)
        plant.user = self.user

        if commit:
            plant.save()
            image = self.cleaned_data.get('image')
            if image:
                PlantImage.objects.create(plant=plant, image=image)
                

        return plant
