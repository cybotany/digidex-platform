from django import forms

from apps.botany.models import Label


class PlantLabelForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter label name'}),
        help_text='The name of the label.',
        error_messages={
            'required': 'Please provide a label name.',
            'max_length': 'Label name should not exceed 100 characters.'
        },
    )

    class Meta:
        model = Label
        fields = ('name',)
