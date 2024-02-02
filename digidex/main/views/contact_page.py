from django.views import View
from django.shortcuts import render, redirect
from digidex.main.forms import ContactForm

class ContactView(View):
    template_name = 'main/contact-page.html'

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
