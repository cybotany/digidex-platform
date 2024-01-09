from django.contrib.auth.views import PasswordResetCompleteView


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
