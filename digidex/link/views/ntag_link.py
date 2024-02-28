import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.link.models import NTAG
from digidex.inventory.models import Plant, Pet
from digidex.inventory.forms import PlantForm, PetForm
from django.contrib import messages

logger = logging.getLogger(__name__)

class NTAGLink(LoginRequiredMixin, DetailView):
    model = NTAG
    template_name = 'inventory/digit/creation-page.html'
    context_object_name = 'ntag'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        ntag = self.object
        linked_digit = ntag.get_digit()

        if ntag.active and linked_digit:
            return redirect(linked_digit.get_absolute_url())

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ntag = self.object
        linked_digit = ntag.get_digit()
        
        if not ntag.active or not linked_digit:
            FormClass, _ = self.get_form_and_model(ntag.use)
            context.update({
                'form': FormClass(**self.get_form_kwargs()),
                'use': ntag.use,
                'kingdom_id': ntag.get_kingdom_id()
            })
        return context

    def get_form_kwargs(self):
        """
        Return the keyword arguments for instantiating the form.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_and_model(self, use):
        if use == 'plant_label':
            return PlantForm, Plant
        elif use in ['dog_tag', 'cat_tag']:
            return PetForm, Pet
        else:
            raise ValueError("Unsupported tag use type")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        ntag = self.object
        FormClass, ModelClass = self.get_form_and_model(ntag.use)
        
        form = FormClass(request.POST, **self.get_form_kwargs())
        if form.is_valid():
            digit = ModelClass.create_digit(form.cleaned_data, ntag, request.user)
            messages.success(request, f"{ModelClass.__name__} created successfully.")
            return redirect(digit.get_absolute_url())
        else:
            messages.error(request, "There was a problem with the form. Please check the details you entered.")
            return self.render_to_response(self.get_context_data(form=form))
    