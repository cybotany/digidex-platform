from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.taxonomy.models import Geography


class LandingView(LoginRequiredMixin, ListView):
    model = Geography
    template_name = 'taxonomy/landing-page.html'
    context_object_name = 'geography_list'
