from django import forms

from apps.botany.models import Plant, Label, PlantImage


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.

    This form allows users to register a new plant with attributes
    such as name, label, common names, and description.
    Users can also upload an image of the plant.
    """

    label = forms.ModelChoiceField(queryset=Label.objects.none(), required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Plant
        fields = ('name', 'label', 'description', 'image')

    def __init__(self, *args, **kwargs):
        """
        Initialize the form.

        Pop the user from kwargs and initializes the queryset for the label
        field to include labels specific to the user as well as common labels.
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            user_labels = Label.objects.filter(user=self.user)
            self.fields['label'].queryset = user_labels

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
