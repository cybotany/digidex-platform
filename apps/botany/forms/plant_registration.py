from django import forms
from apps.botany.models import Plant, PlantImage, Group
from apps.itis.models import TaxonomicUnits


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.
    """
    nfc_tag = forms.CharField(
        required=True,
        widget=forms.HiddenInput()
    )
    tsn = forms.ModelChoiceField(
        queryset=TaxonomicUnits.objects.none(),
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )
    image = forms.ImageField(
        required=False
    )
    group = forms.ModelChoiceField(
        queryset=Group.objects.none(),
        required=False,
        widget=forms.Select(attrs={'id': 'groupField'})
    )

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity', 'tsn', 'group')

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

        self.fields['tsn'].widget.attrs.update({'id': 'tsnField'})
        self.fields['group'].queryset = Group.objects.filter(user=self.user)

    def clean(self):
        cleaned_data = super().clean()
        nfc_value = cleaned_data.get('nfc_tag')

        if not nfc_value:
            raise forms.ValidationError("An NFC Tag is required!")

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
