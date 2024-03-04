from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from digidex.accounts.models import user as digidex_user

class VerificationCheck(View):

    def get(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(digidex_user.DigidexUser, pk=uid)
        token_generator = PasswordResetTokenGenerator()

        if token_generator.check_token(user, token):
            user.email_confirmed = True
            user.save()
            messages.success(request, 'Your email has been verified.')

            return redirect('inventory:update-profile', user_slug=user.slug)
        else:
            return render(request, 'accounts/verification/failure-page.html')
