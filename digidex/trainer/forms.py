from django import forms
from django.core.exceptions import ValidationError


class TrainerForm(forms.Form):
    image = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Short biography'
            }
        ),
        required=False
    )


class DeleteTrainerForm(forms.Form):
    delete = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        ),
        required=True
    )


class TrainerInventoryForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the title of the inventory'
            }
        ),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': 'Provide a detailed description of the object'
            }
        ),
        required=False
    )

    def clean_name(self):
        title = self.cleaned_data['title']
        forbidden_keywords = ['add', 'journal', 'update', 'delete']
        if any(keyword in title.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The title cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')
        return title
