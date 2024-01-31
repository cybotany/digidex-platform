from django.views.generic import TemplateView


class SolutionsView(TemplateView):
    template_name = 'main/solutions-page.html'
