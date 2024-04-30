from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.search import index


class UserDigitizedObject(Orderable):
    user_profile = ParentalKey(
        'accounts.UserProfilePage',
        on_delete=models.PROTECT,
        related_name='user_digits'
    )
    digitized_object = models.OneToOneField(
        'digitization.DigitizedObject',
        on_delete=models.CASCADE,
        related_name='user_associations'
    )


class UserDigitizedObjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'digitization.UserDigitizedObjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class UserDigitizedObjectPage(Page):
    user_digit = models.OneToOneField(
        'digitization.UserDigitizedObject',
        on_delete=models.PROTECT,
        related_name='digit_page'
    )
    user_profile = ParentalKey(
        'accounts.UserProfilePage',
        on_delete=models.PROTECT,
        related_name='digit_pages'
    )
    tags = ClusterTaggableManager(
        through=UserDigitizedObjectPageTag,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_digit_name', partial_match=True, boost=2),
        index.SearchField('get_digit_description', partial_match=True, boost=2),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('user_profile'),
                FieldPanel('tags'),
            ],
            heading="Digit Metadata"
        ),
        FieldPanel('user_digit'),
        InlinePanel('digit_images', label="Digit images"),
    ]

    def get_main_image(self):
        digit_item = self.digit_images.first()
        if digit_item:
            return digit_item.image
        else:
            return None

    def get_digit_name(self):
        """Method to return the name of the digitized object."""
        return self.user_digit.digitized_object.name

    def get_digit_description(self):
        """Method to return the description of the digitized object."""
        return self.user_digit.digitized_object.description


class DigitizedObjectPageGalleryImage(Orderable):
    page = ParentalKey(
        UserDigitizedObjectPage,
        on_delete=models.CASCADE,
        related_name='digitized_object_images'
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


class UserDigitizedObjectTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get('tag')
        digitpages = UserDigitizedObjectPage.objects.filter(tags__name=tag)
        context = super().get_context(request)
        context['digitpages'] = digitpages
        return context
