from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.taxonomy.models import geography as taxon_geography


class LandingView(LoginRequiredMixin, ListView):
    model = taxon_geography.Geography
    template_name = 'taxonomy/landing-page.html'
    context_object_name = 'geography_list'
