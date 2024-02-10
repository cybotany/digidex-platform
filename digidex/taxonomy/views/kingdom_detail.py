from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.taxonomy.models import Kingdom

class KingdomDetailView(LoginRequiredMixin, ListView):
    model = Kingdom
    template_name = 'taxonomy/kingdom-detail-page.html'
    context_object_name = 'kingdoms'
