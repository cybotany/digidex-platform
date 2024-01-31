from django.views.generic import TemplateView


class DetailPostView(TemplateView):
    template_name = 'main/detail-post.html'
