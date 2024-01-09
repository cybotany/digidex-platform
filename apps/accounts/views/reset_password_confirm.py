from django.contrib.auth.views import PasswordResetConfirmView


class DigitPasswordResetConfirmationView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirmation.html'
