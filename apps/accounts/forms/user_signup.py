from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.botany.models import GrowingLabel
from apps.utils.constants import COMMON_LABELS


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            for label in COMMON_LABELS:
                GrowingLabel.objects.create(user=user, name=label, is_common=True)
            user.save()
        return user
