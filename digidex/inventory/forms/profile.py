from django import forms

from base.forms import AssetDeletionCheckbox
from inventory.models import UserProfile


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
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
        model = UserProfile
        fields = ('bio', 'avatar',)


class DeleteUserForm(AssetDeletionCheckbox):
    pass