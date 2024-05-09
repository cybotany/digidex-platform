from django import forms


class UserProfileForm(forms.Form):
    avatar = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
        }),
        required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Short biography'
        }),
        required=False
    )
