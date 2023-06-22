from django import forms

from apps.botany.models import Plant, PlantImage


class PlantUpdateForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Plant
        fields = ['name', 'description', 'images']
    
    def save(self, commit=True):
        instance = super().save(commit)
        for image in self.cleaned_data.get('images', []):
            PlantImage.objects.create(plant=instance, image=image)
        return instance
