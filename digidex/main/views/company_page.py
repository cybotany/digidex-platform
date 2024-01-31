from django.views.generic import TemplateView


class CompanyView(TemplateView):
    template_name = 'main/company-page.html'
