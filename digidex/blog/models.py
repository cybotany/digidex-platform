from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class BlogIndexPage(Page):
    heading_title = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    heading_paragraph = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading_title'),
                FieldPanel('heading_paragraph'),
            ],
            heading="Blog Page Heading",
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
