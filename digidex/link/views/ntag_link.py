from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.link.models import NTAG
from digidex.inventory.models import Plant, Pet
from digidex.inventory.forms import PlantForm, PetForm
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

class NTAGLinkView(LoginRequiredMixin, View):
    def get_object(self):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NTAG, serial_number=serial_number)

    def get_form_and_model(self, tag_use):
        if tag_use == 'plant':
            return PlantForm, Plant, 'inventory/plant/creation-page.html'
        elif tag_use == 'pet':
            return PetForm, Pet, 'inventory/pet/creation-page.html'
        else:
            raise ValueError("Unsupported tag use type")

    def get_associated_digit(self, ntag):
        if ntag.tag_use == 'plant':
            try:
                return ntag.plant
            except Plant.DoesNotExist:
                return None
        elif ntag.tag_use == 'pet':
            try:
                return ntag.pet
            except Pet.DoesNotExist:
                return None
        return None

    def get(self, request, *args, **kwargs):
        ntag = self.get_object()
        associated_digit = self.get_associated_digit(ntag)
        if ntag.active and associated_digit:
            if ntag.user == request.user:
                return HttpResponseRedirect(associated_digit.get_absolute_url())
            else:
                raise PermissionDenied("You do not have permission to view this digit.")
        else:
            FormClass, _, template_name= self.get_form_and_model(ntag.tag_use)
            form = FormClass()
            return render(request, template_name, {'form': form, 'ntag': ntag})

    def post(self, request, *args, **kwargs):
        ntag = self.get_object()
        FormClass, ModelClass, template_name = self.get_form_and_model(ntag.tag_use)
        form = FormClass(request.POST)
        if form.is_valid():
            digit = ModelClass.create_digit(form.cleaned_data, ntag, request.user)
            messages.success(request, f"{ModelClass.__name__} created successfully.")
            return HttpResponseRedirect(digit.get_absolute_url())
        else:
            messages.error(request, "There was a problem with the form. Please check the details you entered.")
            return render(request, template_name, {'form': form, 'ntag': ntag})
    