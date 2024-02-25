from django import forms
from digidex.accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'location', 'is_public',)
        widgets = {
            'avatar': forms.FileInput(attrs={
                'accept': 'image/*',
                'label': 'Upload Avatar',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Short biography',
                'rows': 4,
            }),
            'location': forms.TextInput(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Location',
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'checkbox-input',
                'label': 'Make Profile Public?',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
