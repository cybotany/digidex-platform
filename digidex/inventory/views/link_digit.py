from django.views import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404, render
from digidex.inventory.models import Digit, Link
from digidex.inventory.forms import DigitForm


class LinkDigitView(LoginRequiredMixin, SingleObjectMixin, View):
    model = Link
    slug_field = 'serial_number'
    slug_url_kwarg = 'serial_number'

    def get_object(self, queryset=None):
        # Overriding the method to use 'serial_number' instead of the primary key
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get(self.slug_url_kwarg)
        if serial_number is None:
            raise Http404("No serial number provided")
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get(**{self.slug_field: serial_number})
        except queryset.model.DoesNotExist:
            raise Http404("No Link found matching the query")
        return obj

    def get(self, request, *args, **kwargs):
        link = self.get_object()
        link.increment_counter()

        if not link.active:
            return self.handle_digit_creation(request, link)
        else:
            return self.handle_digit_details(request, link)

    def post(self, request, *args, **kwargs):
        link = self.get_object()
        # Directly call the handle_digit_creation method for POST requests
        return self.handle_digit_creation(request, link)

    def handle_digit_creation(self, request, link):
        form = DigitForm(request.POST)
        if form.is_valid():
            digit = Digit.create_digit(form.cleaned_data, link, request.user)
            return render(request, 'main/digit-details-page.html', {'digit': digit})
        else:
            return render(request, 'main/digit-creation-page.html', {'form': form})

    def handle_digit_details(self, request, link):
        if not link.check_access(request.user):
            return HttpResponseForbidden("Unauthorized access")

        digit = get_object_or_404(Digit, nfc_link=link)
        # Render the digit details template (you can use a different template if needed)
        return render(request, 'main/digit-details-page.html', {'digit': digit})


