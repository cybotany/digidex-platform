from django import views
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect

from nfc.models import NearFieldCommunicationTag


class LinkDigit(views.View):
    template_name = "inventory/digit/creation-page.html"

    def get_object(self):
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(NearFieldCommunicationTag, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        ntag = self.get_object()
        linked_digit = ntag.get_digit()
        if ntag.active and linked_digit:
            return HttpResponseRedirect(linked_digit.get_absolute_url())
        else:
            FormClass, _ = self.get_form_and_model(ntag.use)
            form = FormClass(**self.get_form_kwargs())
            context = {
                'form': form,
                'ntag': ntag
            }
            return render(request, self.template_name, context)
