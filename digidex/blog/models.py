from django import forms
from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

BaseUser = get_user_model()
BaseImage = get_image_model()
BaseDocument = get_document_model()

class BlogIndexPage(Page):
    parent_page_types = ['home.HomePage']
    child_page_types = ['blog.BlogPage']

    intro = models.CharField(
        max_length=250
    )

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogTagIndexPage(Page):

    def get_context(self, request):
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
    child_page_types = []

    date = models.DateField(
        "Post date"
    )
    intro = models.CharField(
        max_length=250
    )
    body = RichTextField(
        blank=True
    )
    authors = ParentalManyToManyField(
        'blog.Author',
        blank=True
    )

    tags = ClusterTaggableManager(
        through=BlogPageTag,
        blank=True
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
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
        BaseImage,
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]


@register_snippet
class Author(models.Model):
    user = models.ForeignKey(
        BaseUser,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('user'),
    ]

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Authors'
