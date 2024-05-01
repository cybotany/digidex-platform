from django import forms

from accounts.models import UserProfile
from wagtail.admin.widgets import RichTextAreaWidget


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        label='Upload Avatar',
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
        }),
        required=False
    )
    body = forms.CharField(
        widget=RichTextAreaWidget(attrs={
            'class': 'text-field base-input',
            'placeholder': 'Short biography'
        }),
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ['avatar', 'description']
