from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.taxonomy.models.itis.taxon import geography as itis_geography

class LandingView(LoginRequiredMixin, ListView):
    model = itis_geography.ItisTaxonGeography
    template_name = 'taxonomy/landing-page.html'
    context_object_name = 'geography_list'
