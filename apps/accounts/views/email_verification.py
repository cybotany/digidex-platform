from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from apps.accounts.models import Profile


class EmailVerificationView(View):

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        email = request.GET.get('email')
        user = get_object_or_404(User, email=email)
        token_generator = PasswordResetTokenGenerator()

        if token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            profile.email_confirmed = True
            profile.save()

            return redirect('inventory:storage')
        else:
            return render(request, 'accounts/failed_verification.html')
