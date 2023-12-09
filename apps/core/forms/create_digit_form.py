from django import forms
from django.db import models
from apps.core.models import Digit
from apps.inventory.models import Group
from apps.taxonomy.models import Unit
from django.contrib.auth import get_user_model


class CreateDigitForm(forms.ModelForm):
    """
    Form for updating an existing digit's details.
    """
    group = forms.ModelChoiceField(
        queryset=Group.objects.none(),
        required=False,
        widget=forms.Select(attrs={'id': 'groupField'})
    )
    taxonomic_unit = forms.ModelChoiceField(
        queryset=Unit.objects.none(),
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )

    class Meta:
        model = Digit
        fields = ('name', 'description', 'group', 'taxonomic_unit')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateDigitForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['group'].queryset = Group.objects.filter(user=user)
