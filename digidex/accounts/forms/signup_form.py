from django import forms
from django.contrib.auth.forms import UserCreationForm
from digidex.accounts.models import User

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Username'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Enter Password Again'
        })

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already associated with a user.")
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username = self.cleaned_data['username'].lower() 
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user
