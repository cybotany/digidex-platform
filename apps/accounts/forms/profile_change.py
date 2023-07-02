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

        # Check if experience is provided but interests is not
        if experience and not interests:
            raise ValidationError("Experience can only be provided if interests are selected.")

        return cleaned_data
