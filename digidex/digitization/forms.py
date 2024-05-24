from django import forms
from django.apps import apps

from digitization.models import DigitalPartyObject, DigitalInventoryObject


UserInventory = apps.get_model('inventory', 'UserInventory')

class DigitalPartyObjectForm(forms.ModelForm):
    class Meta:
        model = DigitalPartyObject
        fields = ('name', 'description',)
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
            )
        }


class DigitalInventoryObjectForm(forms.ModelForm):
    inventory = forms.ModelChoiceField(
        queryset=UserInventory.objects.none(),
        widget=forms.Select(
            attrs={
                'class': 'select-field base-input',
                'placeholder': 'Select an inventory'
            }
        )
    )

    class Meta:
        model = DigitalInventoryObject
        fields = ('name', 'description', 'inventory',)
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
            )
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DigitalInventoryObjectForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['inventory'].queryset = UserInventory.objects.filter(user=user)
