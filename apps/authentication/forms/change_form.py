from django.contrib.auth.forms import UserChangeForm
from ..models import User


class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # update this with the fields on your User model
