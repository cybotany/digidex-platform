from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from apps.accounts.forms import SignupForm


class SignupUserView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('main:landing')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Send verification email
        self.send_verification_email(user)
        return HttpResponseRedirect(reverse('email_confirmation'))

    def send_verification_email(self, user):
        token = PasswordResetTokenGenerator().make_token(user)
        verification_url = reverse('verify-email', kwargs={'token': token})
        full_url = f'http://{self.request.get_host()}{verification_url}'
        send_mail(
            'Verify your email',
            f'Please click the following link to verify your email: {full_url}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
