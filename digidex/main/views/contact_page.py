from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from digidex.main.forms import ContactForm

class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def get(self, request, *args, **kwargs):
        # Disable the form and show a message
        return HttpResponse("The contact form is temporarily disabled. Please check back later.")

    #def form_valid(self, form):
    #    new_contact = form.save()
    #    new_contact.send_email()
    #    return super().form_valid(form)
