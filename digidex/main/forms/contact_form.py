from django import forms
from digidex.main.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'text-field base-input',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'text-field textarea',
                'placeholder': 'Message',
                'rows': 4,
            }),
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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
