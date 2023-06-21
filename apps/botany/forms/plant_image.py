from django import forms
from apps.botany.models import Plant, PlantImage


class PlantImageForm(forms.ModelForm):
    class Meta:
        model = PlantImage
        fields = ('image', 'plant',)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        
        if not image:
            raise forms.ValidationError('You must upload an image.')
            
        if not image.content_type.startswith('image'):
            raise forms.ValidationError('File type is not image.')
            
        return image

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PlantImageForm, self).__init__(*args, **kwargs)
        
        # Limit the plant field to only the plants owned by the logged in user
        self.fields['plant'].queryset = Plant.objects.filter(owner=self.request.user)
