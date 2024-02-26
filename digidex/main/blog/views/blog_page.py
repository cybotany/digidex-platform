from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'main/blog-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'subtitle': 'Blog',
            'heading': "News and Updates",
            'paragraph': "Egestas ac in semper pharetra sed."
        })
        return context
