from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from digidex.utils.helpers import validate_recaptcha
from digidex.main.forms import ContactForm
import logging

logger = logging.getLogger(__name__)

class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def form_valid(self, form):
        recaptcha_token = self.request.POST.get('g-recaptcha-response')
        validation_result = validate_recaptcha(recaptcha_token, 'submit_contactForm')

        if not validation_result.get("success"):
            logger.warning(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            return HttpResponseRedirect(reverse_lazy('main:error'))

        form.save()
        return super().form_valid(form)
