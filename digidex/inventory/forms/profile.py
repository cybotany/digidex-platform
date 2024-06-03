from django import forms

from base.forms import AssetDeletionCheckbox
from inventory.models import UserProfilePage


class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Short biography'
            }
        ),
        required=False
    )

    class Meta:
        model = UserProfilePage
        fields = ('bio', 'image',)


class DeleteUserForm(AssetDeletionCheckbox):
    pass
