from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.search.index import SearchField


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    authors = ParentalManyToManyField(
        'blog.Author',
        blank=True
    )
    tags = ClusterTaggableManager(
        through=BlogPageTag,
        blank=True
    )
    heading = models.CharField(
        max_length=250
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

    search_fields = Page.search_fields + [
        FieldPanel('intro'),
        SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('date'),
                FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
                FieldPanel('tags'),
            ],
            heading="Blog information"
        ),
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
