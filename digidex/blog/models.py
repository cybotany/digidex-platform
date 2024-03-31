from modelcluster.fields import ParentalKey

from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index

from modelcluster.fields import ParentalKey

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


class BlogPage(Page):
    date = models.DateField("Post date")
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
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('heading_title'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('heading_title'),
        FieldPanel('heading_paragraph'),
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
