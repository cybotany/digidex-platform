from django import forms
from apps.core.models import Digit, Journal


class CreateDigitForm(forms.ModelForm):
    """
    Form for updating an existing digit's details.
    """
    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Digit
        fields = ('name', 'description', 'group', 'link', 'taxonomic_unit', 'user')

    def __init__(self, *args, **kwargs):
        super(CreateDigitForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Save the form's fields to the associated model.
        """
        digit = super().save(commit)

        #image = self.cleaned_data.get('image')
        #if image:
        #    DigitImage.objects.create(digit=digit, image=image)
        
        return digit
