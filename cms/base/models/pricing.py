from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from taggit.models import TaggedItemBase

class PricingIndexPage(Page):
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        pricing_pages = self.get_children().live().order_by('-first_published_at')
        context['pricing_pages'] = {
            'latest': None,
            'older': [],
        }
        if pricing_pages.exists():
            context['pricing_pages']['latest'] = pricing_pages.first()
            context['pricing_pages']['older'] = pricing_pages[1:]
        return context


class PricingPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'PricingPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class PricingTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get('tag')
        pricing_pages = PricingPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['pricing_pages'] = pricing_pages
        return context


class PricingPage(Page):
    date = models.DateField(
        "Post date"
    )
    intro = models.CharField(
        max_length=250
    )
    body = RichTextField(
        blank=True
    )
    tags = ClusterTaggableManager(
        through=PricingPageTag,
        blank=True
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def solution_index(self):
        return self.get_ancestors().type(PricingIndexPage).last()


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Pricing Information"),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class PricingPageGalleryImage(Orderable):
    page = ParentalKey(
        PricingPage,
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
