from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationView(View):

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        user = get_object_or_404(User, email=request.GET.get('email'))
        token_generator = PasswordResetTokenGenerator()

        if token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            # Redirect to a success page or login page 
            return redirect('some-success-url')
        else:
            # Handle invalid token
            return render(request, 'email_verification_failed.html')
