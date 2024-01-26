from django import forms
from digidex.main.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }
        help_texts = {
            'name': 'Enter your full name.',
            'email': 'Enter your email address.',
            'message': 'Write your message here.',
        }
        error_messages = {
            'name': {
                'max_length': "This name is too long.",
                'required': "Name is required."
            },
            'email': {
                'invalid': "Enter a valid email address.",
                'required': "Email is required."
            },
            'message': {
                'required': "Please enter a message."
            },
        }
