from django.contrib.auth.views import PasswordResetConfirmView


class PasswordResetConfirmationView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirmation.html'
