from modelcluster.fields import ParentalKey

from django.db import models
from wagtail import fields
from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.search import index
from modelcluster.fields import ParentalKey

class BlogIndexPage(wt_models.Page):
    heading = fields.RichTextField(blank=True)
    intro = fields.RichTextField(blank=True)

    content_panels = wt_models.Page.content_panels

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(wt_models.Page):
    heading = fields.RichTextField(blank=True)
    intro = fields.RichTextField(blank=True)
    date = models.DateField("Post date")
    body = fields.RichTextField(blank=True)

    search_fields = wt_models.Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('date'),
        panels.FieldPanel('body'),
        panels.InlinePanel('gallery_images', label="Gallery images"),
    ]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


class BlogPageGalleryImage(wt_models.Orderable):
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
        panels.FieldPanel('image'),
        panels.FieldPanel('caption'),
    ]
