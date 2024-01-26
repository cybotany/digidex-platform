from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from digidex.main.forms import ContactForm


class ContactUsView(View):
    template_name = 'main/contact-page.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()

            send_mail(
                subject=f"New Contact Us Message from {new_contact.name}",
                message=new_contact.message,
                from_email=new_contact.email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

        return redirect('main:thanks')
