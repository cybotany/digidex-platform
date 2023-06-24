from django import forms
from apps.cea.models import Greenhouse


class GreenhouseRegistrationForm(forms.ModelForm):
    """
    Form for creating a new Greenhouse.

    Attributes:
        name (CharField): The name of the label.
    """
    class Meta:
        model = Greenhouse
        fields = ('name', 'description', 'location',)
