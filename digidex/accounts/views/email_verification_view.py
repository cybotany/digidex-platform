from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from digidex.accounts.models import User


class EmailVerificationView(View):

    def get(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        token_generator = PasswordResetTokenGenerator()

        if token_generator.check_token(user, token):
            user.email_confirmed = True
            user.save()
            messages.success(request, 'Your email has been verified. You may now log in.')

            return redirect('inventory:digit-storage')
        else:
            return render(request, 'accounts/failed-verification-page.html')
