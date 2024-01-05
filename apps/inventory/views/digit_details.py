from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit


class DigitDetailsView(LoginRequiredMixin, DetailView):
    model = Digit
    template_name = 'inventory/digit_details.html'
