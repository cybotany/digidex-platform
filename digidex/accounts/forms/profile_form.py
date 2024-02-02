from django import forms
from digidex.accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar',)
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Short biography',
                'rows': 4,
            }),
            'location': forms.TextInput(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Location',
            }),
            'avatar': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'base-file-upload-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Optionally, you can add more dynamic attributes or processing here
