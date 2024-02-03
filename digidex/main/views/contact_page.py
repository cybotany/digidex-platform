from django.views import View
from django.shortcuts import render, redirect
from digidex.main.forms import ContactForm

class ContactView(View):
    template_name = 'main/contact-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Contact Us'
        context['heading'] = "Have questions? Contact us for assistance"
        context['paragraph'] = "We're here to help!"
        return context

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:thanks')
        else:
            return render(request, self.template_name, {'form': form})
