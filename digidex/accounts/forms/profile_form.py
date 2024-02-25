from django import forms
from digidex.accounts.models import Profile

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
        })
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Short biography',
            'rows': 4,
        }),
        required=False
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Location',
        }),
        required=False
    )
    is_public = forms.BooleanField(
        label='Make Profile Public?',
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
        }),
        required=False 
    )

    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'location', 'is_public',)
