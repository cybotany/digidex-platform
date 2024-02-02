from django import forms
from django.contrib.auth.forms import AuthenticationForm
from digidex.accounts.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Username'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Password'
        })

    def clean_username(self):
        ''' 
        Usernames are case insensitive, so we need to convert the username to lowercase before
        checking if it exists in the database
        '''
        username = self.cleaned_data['username']
        username_lower = username.lower()
        if not User.objects.filter(username__iexact=username_lower).exists():
            raise forms.ValidationError("Invalid username: %s" % username)

        return username_lower
