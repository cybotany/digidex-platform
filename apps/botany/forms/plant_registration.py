from django import forms
from apps.botany.models import Plant, PlantImage, Group


class PlantRegistrationForm(forms.ModelForm):
    """
    Form for users to register their plant.
    """
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
        self.user = kwargs.pop('user', None)
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        self.fields['group'].queryset = Group.objects.filter(user=self.user)


    def save(self, commit=True):
        """
        Save the form.
        """
        plant = super().save(commit)

        image = self.cleaned_data.get('image')
        if image:
            PlantImage.objects.create(plant=plant, image=image)
            
        return plant
