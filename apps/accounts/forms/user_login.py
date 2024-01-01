from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):

    def clean_username(self):
        username = self.cleaned_data['username']

        # Convert the username to lowercase
        username_lower = username.lower()

        # Check if the lowercase username exists in the database
        if not User.objects.filter(username__iexact=username_lower).exists():
            raise forms.ValidationError("Invalid username")

        return username_lower
