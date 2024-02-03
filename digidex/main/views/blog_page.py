from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'main/blog-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Blog'
        context['heading'] = 'News and Updates'
        context['paragraph'] = 'Egestas ac in semper pharetra sed.'
        return context
