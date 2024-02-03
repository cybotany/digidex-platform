from django.views.generic import TemplateView


class CompanyView(TemplateView):
    template_name = 'main/company-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'About Us'
        context['heading'] = "Who we are and why we're doing this"
        context['paragraph'] = 'Nurturing the Future of Biodiversity Through Innovation and Passion'
        return context