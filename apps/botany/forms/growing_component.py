from django import forms
from apps.botany.models import GrowingMediumComponent


class GrowingComponentForm(forms.ModelForm):
    """
    Form for creating a new growing medium component.

    Attributes:
        component (CharField): The type of growing medium component.
        description (CharField): The description of the growing medium component.
        particle_size (DecimalField): The particle size of the growing medium component.
        particle_size_unit (CharField): The unit of measurement for the particle size.
    """
    component = forms.ChoiceField(
        choices=GrowingMediumComponent.component.field.choices,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select component'
            }
        ),
        help_text='Components used as growing medium for plants.',
        error_messages={
            'required': 'Please select a component.',
        },
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }
        ),
        help_text='Description for plant growing medium components.',
        required=False,
    )
    particle_size = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter particle size'
            }
        ),
        help_text='Particle size of the growing medium component.',
        required=False,
    )
    particle_size_unit = forms.ChoiceField(
        choices=GrowingMediumComponent.particle_size_unit.field.choices,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select unit'
            }
        ),
        help_text='Unit of measurement for the particle size.',
        required=False,
    )

    class Meta:
        """
        Meta class for the GrowingMediumComponentForm.

        Attributes:
            model (Model): The model class to associate with this form.
            fields (tuple): Fields to be included in this form.
        """
        model = GrowingMediumComponent
        fields = ('component', 'description', 'particle_size', 'particle_size_unit')
