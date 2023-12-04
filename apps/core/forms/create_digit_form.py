from django import forms
from django.db import models
from apps.core.models import Digit
from apps.inventory.models import Link, Group
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
        fields = ('name', 'description', 'group', 'link', 'taxonomic_unit')

    def __init__(self, *args, **kwargs):
            super(CreateDigitForm, self).__init__(*args, **kwargs)
            # Dynamically set querysets or initial values here
