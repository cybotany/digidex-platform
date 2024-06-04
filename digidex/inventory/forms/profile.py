from django import forms

from base.forms import AssetDeletionCheckbox


class UserProfileForm(forms.Form):
    image = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Short biography'
            }
        ),
        required=False
    )

class DeleteUserForm(AssetDeletionCheckbox):
    pass
