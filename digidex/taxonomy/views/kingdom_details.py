from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.taxonomy.models import Kingdom


class KingdomDetailsView(LoginRequiredMixin, DetailView):
    model = Kingdom
    template_name = 'taxonomy/kingdom-details-page.html'
    context_object_name = 'kingdom'
