from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'cybotany/home.html'
