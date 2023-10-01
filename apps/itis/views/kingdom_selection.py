from django.views.generic import TemplateView
from apps.itis.models import Kingdoms


class KingdomDropdownView(TemplateView):
    template_name = 'itis/kingdoms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kingdoms'] = Kingdoms.objects.all()
        print(context['kingdoms'])
        return context