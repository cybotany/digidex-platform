from django import forms
from apps.botany.models import GrowingLabel


class GrowingLabelForm(forms.ModelForm):
    """
    Form for creating a new label for plants.

    Attributes:
        name (CharField): The name of the label.
    """

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter label name'
            }
        ),
        help_text='The name of the label.',
        error_messages={
            'required': 'Please provide a label name.',
            'max_length': 'Label name should not exceed 100 characters.'
        },
    )

    class Meta:
        """
        Meta class for the GrowingLabelForm.

        Attributes:
            model (Model): The model class to associate with this form.
            fields (tuple): Fields to be included in this form.
        """

        model = GrowingLabel
        fields = ('name',)
