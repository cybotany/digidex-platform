from django.views.generic import TemplateView


class DetailCategoryView(TemplateView):
    template_name = 'main/detail_category.html'
