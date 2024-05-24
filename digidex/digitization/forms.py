from django import forms
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()
UserInventory = apps.get_model('inventory', 'UserInventory')
UserParty = apps.get_model('party', 'UserParty')
DigitalObject = apps.get_model('digitization', 'DigitalObject')
ContentType = apps.get_model('contenttypes', 'ContentType')


class DigitalObjectForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the digitized object'
            }
        )
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
    inventory = forms.ModelChoiceField(
        queryset=UserInventory.objects.none(),
        widget=forms.Select(
            attrs={
                'class': 'select-field base-input',
                'placeholder': 'Select an inventory'
            }
        ),
        required=False
    )
    party = forms.ModelChoiceField(
        queryset=UserParty.objects.none(),
        widget=forms.HiddenInput(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DigitalObjectForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['inventory'].queryset = UserInventory.objects.filter(user=user)
            self.fields['party'].queryset = UserParty.objects.filter(user=user)
            if self.fields['party'].queryset.exists():
                self.fields['party'].initial = self.fields['party'].queryset.first().pk
        self.user = user

    def save(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data.get('description', '')
        inventory = self.cleaned_data.get('inventory')
        party = self.cleaned_data.get('party')

        if not inventory and not party:
            raise forms.ValidationError("You must select either an inventory or a party.")

        content_object = inventory if inventory else UserParty.objects.get(pk=party)
        content_type = ContentType.objects.get_for_model(content_object)

        digital_object = DigitalObject.objects.create(
            name=name,
            description=description,
            content_type=content_type,
            object_id=content_object.id,
        )

        return digital_object
