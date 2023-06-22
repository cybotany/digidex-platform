from django import forms

from apps.botany.models import Plant, Label, PlantImage


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.
    """
    label = forms.ModelChoiceField(queryset=Label.objects.none(), required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Plant
        fields = ('name', 'label', 'common_names', 'description', 'image')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        user_labels = Label.objects.filter(user=self.user)
        common_labels = Label.get_common_labels()
        self.fields['label'].queryset = user_labels | common_labels

    def save(self, commit=True):
        plant = super().save(commit=False)
        plant.owner = self.user
        if commit:
            plant.save()
            # Save the uploaded image
            image = self.cleaned_data.get('image')
            if image:
                PlantImage.objects.create(plant=plant, image=image)

        return plant
