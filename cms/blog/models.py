from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # Get all live blog pages children of this page, ordered by publish date
        blogpages = self.get_children().live().order_by('-first_published_at')
        # Initialize the blogpages dict in context
        context['blogpages'] = {
            'latest': None,
            'older': [],
        }
        # If there are any blog pages, assign latest and older accordingly
        if blogpages.exists():
            context['blogpages']['latest'] = blogpages.first()
            context['blogpages']['older'] = blogpages[1:]
        return context



class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()
