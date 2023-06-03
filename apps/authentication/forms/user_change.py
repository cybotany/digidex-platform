from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class ChangeForm(UserChangeForm):
    '''
    This form is to change information used to authenticate users.
    '''
    class Meta:
        model = User
        fields = ('email',)
