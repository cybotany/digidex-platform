from django import forms
from apps.botany.models import Fertilizer


class GrowingFertilizerForm(forms.ModelForm):
    """
    Form for creating a new fertilizer mix.

    Attributes:
        name (CharField): The name of the fertilizer mix.
        description (CharField): The description of the fertilizer mix.
        components (CharField): The components of the fertilizer mix.
        nutrient_content (CharField): The nutrient content of the fertilizer mix.
    """

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter fertilizer mix name'
            }
        ),
        help_text='The name of the fertilizer mix.',
        error_messages={
            'required': 'Please provide a fertilizer mix name.',
            'max_length': 'Fertilizer mix name should not exceed 100 characters.'
        },
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter a description for the fertilizer mix'
            }
        ),
        help_text='Description for the fertilizer mix.',
    )

    components = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the components of the fertilizer mix'
            }
        ),
        help_text='Components used in the fertilizer mix.',
    )

    nutrient_content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter nutrient content of the fertilizer mix'
            }
        ),
        help_text='Nutrient content of the fertilizer mix.',
    )

    class Meta:
        """
        Meta class for the FertilizerMixForm.

        Attributes:
            model (Model): The model class to associate with this form.
            fields (tuple): Fields to be included in this form.
        """

        model = FertilizerMix
        fields = ('name', 'description', 'components', 'nutrient_content')
