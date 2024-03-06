from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
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
    date = models.DateField(
        "Post date"
    )
    intro = models.CharField(
        max_length=250
    )
    body = RichTextField(
        blank=True
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),

        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(
        BlogPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(
        blank=True,
        max_length=250
    )

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]