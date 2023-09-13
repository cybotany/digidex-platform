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
    sow_date = forms.DateTimeField(required=False)

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'nfc_tag', 'grouping')

    def __init__(self, *args, **kwargs):
            """
            Initialize the form.

            Pop the user and nfc_tag from kwargs.
            """
            self.user = kwargs.pop('user', None)
            self.nfc_tag = kwargs.pop('nfc_tag', None)
            super().__init__(*args, **kwargs)

            if self.nfc_tag:
                self.fields['nfc_tag'].initial = self.nfc_tag

            self.fields['sow_date'].widget = forms.HiddenInput()
            self.fields['sow_date'].required = False

            if self.instance.grouping == 'Seed':
                self.fields['sow_date'].widget = forms.DateTimeInput()
                self.fields['sow_date'].required = True

    def clean(self):
        """
        Clean the form.

        If the grouping is 'Seed', ensure that the sow_date is provided.
        """
        cleaned_data = super().clean()
        grouping = cleaned_data.get('grouping')
        sow_date = cleaned_data.get('sow_date')

        if grouping == 'Seed' and not sow_date:
            self.add_error('sow_date', 'Sow date is required.')

        return cleaned_data

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
