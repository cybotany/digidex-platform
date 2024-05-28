from django import forms

from digitization.models import DigitalObject
from inventory.models import Category


class InventoryCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the inventory'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            )
        }


class ItemizedDigitForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'dropdown',
                'placeholder': 'Select a category'
            }
        )
    )

    class Meta:
        model = DigitalObject
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'text-field base-input',
                    'placeholder': 'Enter the name of the digitized object'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'text-field textarea',
                    'placeholder': 'Provide a detailed description of the object'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ItemizedDigitForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)