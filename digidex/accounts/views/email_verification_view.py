from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, force_text
from digidex.accounts.models import User


class EmailVerificationView(View):

    def get(self, request, uidb64, token):
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        token_generator = PasswordResetTokenGenerator()

        if token_generator.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()

            return redirect('inventory:digit-storage')
        else:
            return render(request, 'accounts/failed-verification-page.html')
