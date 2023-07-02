from django import forms
from django.core.exceptions import ValidationError

from apps.accounts.models import Profile


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'avatar', 'interests', 'experience',)

    def clean(self):
        cleaned_data = super().clean()
        interests = cleaned_data.get('interests')
        experience = cleaned_data.get('experience')

        if bool(interests) != bool(experience):
            raise ValidationError("Both interests and experience must be provided, or both must be left empty.")

        return cleaned_data
