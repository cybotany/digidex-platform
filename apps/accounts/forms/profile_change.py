from django import forms
from apps.accounts.models import Profile


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar',)
