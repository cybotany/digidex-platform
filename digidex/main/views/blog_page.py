from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'main/blog-page.html'
