from wagtail import models as wt_models
from wagtail import fields
from wagtail.admin import panels

from blog import blocks

class BlogIndexPage(wt_models.Page):
    body = fields.StreamField(
        blocks.BlogStreamBlock(),
        blank=True,
        use_json_field=True
    )

    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')

        if blogpages:
            context['featured_post'] = blogpages[0]
            context['blogpages'] = blogpages[1:]
        else:
            context['empty_blog'] = True

        return context