from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from digidex.main.forms import ContactForm

class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'subtitle': 'Contact',
            'heading': "Contact us for assistance",
            'paragraph': "We're here to help!"
        })
        return context

    def form_valid(self, form):
        new_contact = form.save()
        new_contact.send_email()
        return super().form_valid(form)
