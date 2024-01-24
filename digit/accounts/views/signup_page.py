from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db import transaction
from digit.accounts.forms import SignupForm


class SignupUserView(FormView):
    template_name = 'main/signup-page.html'
    form_class = SignupForm
    success_url = reverse_lazy('main:landing')

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Send verification email
            self.send_verification_email(user)

        return HttpResponseRedirect(reverse('accounts:confirm-email'))

    def send_verification_email(self, user):
        token = PasswordResetTokenGenerator().make_token(user)
        base_url = reverse('accounts:verify-email')
        query_string = urlencode({'token': token, 'email': user.email})
        full_url = f'http://{self.request.get_host()}{base_url}?{query_string}'

        send_mail(
            'Verify your email',
            f'Please click the following link to verify your email: {full_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
