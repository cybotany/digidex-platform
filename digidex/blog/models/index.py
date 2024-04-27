from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from blog.blocks import BlogStreamBlock

class BlogIndexPage(Page):
    body = StreamField(
        BlogStreamBlock(),
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
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
