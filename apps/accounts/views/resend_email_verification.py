from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class ResendVerificationEmailView(View):
    def get(self, request):
        # Display a form for user to enter their email
        return render(request, 'resend_verification_email.html')

    def post(self, request):
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)

        # Generate token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        # Construct verification URL
        verification_url = request.build_absolute_uri(
            reverse('accounts:verify-email', kwargs={'uidb64': uid, 'token': token})
        )

        send_mail(
            'Verify Your Email',
            f'Please click on the link to verify your email: {verification_url}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        # Redirect to confirmation page
        return redirect('accounts:email-confirmation')
