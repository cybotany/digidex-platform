from django import forms
from django.core.exceptions import ValidationError

from category.models import CategoryPage


class CategoryPageForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter a name'
            }
        ),
        required=True
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': '(Optional) Provide a description'
            }
        ),
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_keywords = ['add', 'update', 'delete', 'remove', 'edit', 'create', 'destroy', 'new', 'old', 'current', 'previous', 'next', 'last', 'first', 'all', 'any', 'some',]
        if any(keyword in name.lower() for keyword in forbidden_keywords):
            raise ValidationError(f'The name cannot contain any of the following keywords: {", ".join(forbidden_keywords)}')
        return name

    class Meta:
        model = CategoryPage
        fields = ['name', 'body']


class DeleteCategoryPageForm(forms.Form):
    delete = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        ),
        required=True
    )
