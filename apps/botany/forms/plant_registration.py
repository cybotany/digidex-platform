from django import forms
from apps.botany.models import Plant, PlantImage


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.
    """
    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Plant
        fields = ('name', 'description', 'image', 'quantity')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        """
        Save the form.
        """
        plant = super().save(commit)

        image = self.cleaned_data.get('image')
        if image:
            PlantImage.objects.create(plant=plant, image=image)
            
        return plant
