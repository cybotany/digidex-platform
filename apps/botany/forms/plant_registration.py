from django import forms
from apps.botany.models import Plant, PlantImage, Group
from apps.nfc.models import Tag


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
        self.user = kwargs.pop('user', None)
        self.nfc_tag = kwargs.pop('nfc_tag', None)
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.filter(user=self.user)


    def save(self, commit=True):
        """
        Save the form.
        """
        plant = super().save(commit=False)
        plant.user = self.user  # Set the user

        # Handle NFC Tag
        nfc_tag_sn = self.cleaned_data.get('nfc_tag')
        if nfc_tag_sn:
            tag, created = Tag.objects.get_or_create(
                serial_number=nfc_tag_sn,
                defaults={'created_by': self.user, 'active': True}
            )
            plant.nfc_tag = tag.serial_number  # Assuming nfc_tag is a CharField on Plant

        if commit:
            plant.save()
            image = self.cleaned_data.get('image')
            if image:
                PlantImage.objects.create(plant=plant, image=image)
            
        return plant
            
            
        return plant
