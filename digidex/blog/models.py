from django.db import models
from django import forms

from modelcluster import fields as mc_fields

from wagtail import fields
from wagtail import models as wt_models
from wagtail.admin import panels
from wagtail.search import index
from wagtail.snippets import models as wt_snippets

class BlogIndexPage(wt_models.Page):
    heading = models.CharField(max_length=250)
    intro = models.CharField(max_length=250)

    content_panels = wt_models.Page.content_panels + [
        panels.FieldPanel('heading'),
        panels.FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')

        if blogpages:
            context['featured_post'] = blogpages[0]
            context['blogpages'] = blogpages[1:]
        else:
            context['empty_blog'] = True

        return context


class BlogPage(wt_models.Page):
    heading = models.CharField(max_length=250)
    intro = models.CharField(max_length=250)

    date = models.DateField("Post date")
    body = fields.RichTextField(blank=True)
    authors = mc_fields.ParentalManyToManyField(
        'blog.Author',
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
            ],
            heading="Blog information"
        ),
        panels.FieldPanel('heading'),
        panels.FieldPanel('intro'),
        panels.FieldPanel('body'),
        panels.InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(wt_models.Orderable):
    page = mc_fields.ParentalKey(
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


@wt_snippets.register_snippet
class Author(models.Model):
    name = models.CharField(
        max_length=255
    )
    author_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        panels.FieldPanel('name'),
        panels.FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'
