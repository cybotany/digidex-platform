from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from taggit.models import TaggedItemBase

class SolutionIndexPage(Page):
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        solution_pages = self.get_children().live().order_by('-first_published_at')
        context['solution_pages'] = {
            'latest': None,
            'older': [],
        }
        if solution_pages.exists():
            context['solution_pages']['latest'] = solution_pages.first()
            context['solution_pages']['older'] = solution_pages[1:]
        return context


class SolutionPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'SolutionPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class SolutionTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get('tag')
        solution_pages = SolutionPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['solution_pages'] = solution_pages
        return context


class SolutionPage(Page):
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
        through=SolutionPageTag,
        blank=True
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def solution_index(self):
        return self.get_ancestors().type(SolutionIndexPage).last()


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Solution Information"),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class SolutionPageGalleryImage(Orderable):
    page = ParentalKey(
        SolutionPage,
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
