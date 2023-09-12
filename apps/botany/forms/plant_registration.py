from django import forms
from django.forms.widgets import TextInput
from apps.botany.models import Plant, GrowingLabel, PlantImage


class ReadOnlyTextInput(TextInput):
    """
    A read-only text input widget.
    """
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'readonly': 'readonly'}
        super().__init__(*args, **kwargs)


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.

    This form allows users to register a new plant with attributes
    such as name, label, common names, and description.
    Users can also upload an image of the plant.
    """

    nfc_tag = forms.CharField(widget=ReadOnlyTextInput, required=False)
    label = forms.ModelChoiceField(queryset=GrowingLabel.objects.none(), required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Plant
        fields = ('name', 'label', 'description', 'image', 'nfc_tag')

    def __init__(self, *args, **kwargs):
            """
            Initialize the form.

            Pop the user and id from kwargs and initializes the queryset for the label
            field to include labels specific to the user as well as common labels.
            """
            self.user = kwargs.pop('user', None)
            self.nfc_tag = kwargs.pop('nfc_tag', None)
            super().__init__(*args, **kwargs)

            if self.user:
                user_labels = GrowingLabel.objects.filter(user=self.user)
                self.fields['label'].queryset = user_labels

            if self.nfc_tag:
                self.fields['nfc_tag'].initial = self.nfc_tag

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
