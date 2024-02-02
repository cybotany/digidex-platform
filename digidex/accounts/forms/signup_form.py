from django import forms
from django.contrib.auth.forms import UserCreationForm
from digidex.accounts.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'text-field base-input',
        'placeholder': 'Email'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Repeat Password'
        })

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
