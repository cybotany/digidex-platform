from django.contrib.auth.views import PasswordResetView


class PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
