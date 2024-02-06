from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from digidex.api.utils import validate_recaptcha
from digidex.main.forms import ContactForm


class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def form_valid(self, form):
        # Retrieve the reCAPTCHA token and response from the request
        recaptcha_token = self.request.POST.get('g-recaptcha-response')
        recaptcha_action = self.request.POST.get('recaptcha_action')

        # Validate the token
        response = validate_recaptcha(recaptcha_token, recaptcha_action)

        if response and response.risk_analysis.score >= settings.RECAPTCHA_REQUIRED_SCORE:
            new_contact = form.save()
            new_contact.send_email()
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('main:contact_error'))
