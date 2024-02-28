import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.link.models import NTAG
from digidex.inventory.models import Plant, Pet
from digidex.inventory.forms import PlantForm, PetForm
from django.contrib import messages

logger = logging.getLogger(__name__)

class NTAGLink(LoginRequiredMixin, View):
    def get_form_kwargs(self):
        """
        Return the keyword arguments for instantiating the form.
        """
        kwargs = super(NTAGLink, self).get_form_kwargs() if hasattr(super(), 'get_form_kwargs') else {}
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NTAG, serial_number=serial_number)

    def get_form_and_model(self, use):
        if use == 'plant':
            return PlantForm, Plant
        elif use == 'pet':
            return PetForm, Pet
        else:
            raise ValueError("Unsupported tag use type")

    def get(self, request, *args, **kwargs):
        ntag = self.get_object()
        linked_digit = ntag.get_digit_type()
        if ntag.active and linked_digit:
            return HttpResponseRedirect(linked_digit.get_absolute_url())
        else:
            FormClass, _= self.get_form_and_model(ntag.get_link_use())
            form = FormClass(**self.get_form_kwargs())
            template_name = f"inventory/digit/{ntag.get_link_use()}/creation_page.html"
            return render(request, template_name, {'form': form, 'ntag': ntag})

    def post(self, request, *args, **kwargs):
        ntag = self.get_object()
        FormClass, ModelClass = self.get_form_and_model(ntag.get_link_use())
        template_name = f"inventory/digit/{ntag.get_link_use()}/creation_page.html"
        form = FormClass(request.POST, **self.get_form_kwargs())
        if form.is_valid():
            digit = ModelClass.create_digit(form.cleaned_data, ntag, request.user)
            messages.success(request, f"{ModelClass.__name__} created successfully.")
            return HttpResponseRedirect(digit.get_absolute_url())
        else:
            messages.error(request, "There was a problem with the form. Please check the details you entered.")
            return render(request, template_name, {'form': form, 'ntag': ntag})
    