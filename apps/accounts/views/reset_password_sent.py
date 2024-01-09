from django.contrib.auth.views import PasswordResetDoneView


class PasswordResetSentView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_sent.html'
