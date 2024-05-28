from django import forms

from inventory.models import Category, ItemizedDigit


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
    class Meta:
        model = ItemizedDigit
        fields = ['name', 'description',]
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