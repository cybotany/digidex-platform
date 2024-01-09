from django.contrib.auth.views import PasswordResetView


class DigitPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/partials/password_reset_email.html'