from django.db import models
from django import forms

from modelcluster import fields as mc_fields
from modelcluster.contrib import taggit as mc_taggit
from taggit import models as tg_models

from wagtail import fields
from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.search import index

class BlogPageTag(tg_models.TaggedItemBase):
    content_object = mc_fields.ParentalKey(
        'blog.BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(wt_models.Page):
    date = models.DateField("Post date")
    authors = mc_fields.ParentalManyToManyField(
        'blog.Author',
        blank=True
    )
    tags = mc_taggit.ClusterTaggableManager(
        through=BlogPageTag,
        blank=True
    )
    heading = models.CharField(
        max_length=250
    )
    intro = models.CharField(
        max_length=250
    )
    body = fields.RichTextField(
        blank=True
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = wt_models.Page.search_fields + [
        panels.FieldPanel('intro'),
        index.SearchField('body'),
    ]

    content_panels = wt_models.Page.content_panels + [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('date'),
                panels.FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
                panels.FieldPanel('tags'),
            ],
            heading="Blog information"
        ),
        panels.FieldPanel('heading'),
        panels.FieldPanel('intro'),
        panels.FieldPanel('body'),
        panels.InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogTagIndexPage(wt_models.Page):

    def get_context(self, request):
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
