from django import forms
from apps.inventory.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
