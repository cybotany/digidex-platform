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

    name = forms.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized plant."
    )
    description = forms.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="A brief description of the digitized plant."
    )
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.CASCADE,
        related_name='digits',
        help_text="The group to which the digitized plant belongs."
    )
    link = models.OneToOneField(
        Link,
        on_delete=models.CASCADE,
        related_name='digit',
        help_text="The NFC tag link associated with the digitized plant."
    )
    taxonomic_unit = forms.ModelChoiceField(
        queryset=Unit.objects.none(),
        required=False,
        widget=forms.TextInput(attrs={'id': 'tsnField'})
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="The user who created the digitized plant record."
    )

    class Meta:
        model = Digit
        fields = ('name', 'description', 'group', 'link', 'taxonomic_unit', 'user')
