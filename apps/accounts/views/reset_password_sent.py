from django.contrib.auth.views import PasswordResetDoneView


class DigitPasswordResetSentView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_sent.html'
