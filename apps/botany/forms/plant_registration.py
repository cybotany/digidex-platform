from django import forms
from apps.botany.models import Plant, PlantImage, Group


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.
    """
    nfc_tag = forms.CharField(
        required=True,
        widget=forms.HiddenInput()
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
        fields = ('name', 'description', 'image', 'quantity', 'group')

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

        self.fields['group'].queryset = Group.objects.filter(user=self.user)

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
