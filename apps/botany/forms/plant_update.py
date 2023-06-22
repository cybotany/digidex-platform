from django import forms

from apps.botany.models import Plant, PlantImage


class PlantUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Plant
        fields = ['name', 'description', 'image']

    def save(self, commit=True):
        instance = super().save(commit)

        # Get the uploaded image
        image = self.cleaned_data.get('image')

        # Save the image to the PlantImage model if it exists
        if image:
            PlantImage.objects.create(plant=instance, image=image)
        return instance
