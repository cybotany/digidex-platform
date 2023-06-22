from django import forms

from apps.botany.models import Plant, Label, PlantImage


class PlantRegistrationForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=Label.objects.none(), required=False)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Plant
        fields = ('name', 'label', 'common_names', 'description', 'images')

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
            # Save the uploaded images
            for image in self.cleaned_data.get('images', []):
                PlantImage.objects.create(plant=plant, image=image)
        return plant
