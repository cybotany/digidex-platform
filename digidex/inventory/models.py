from django.db import models, transaction
from django.utils.text import slugify

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index


class UserDigitizedObjectInventoryPage(Page):
    intro = models.TextField(
        blank=True,
        help_text="Introduction text to display at the top of the index page."
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('itemized_digits', label="Digits in Inventory"),
    ]

    parent_page_types = [
        'accounts.UserProfilePage'
    ]

    subpage_types = [
        'inventory.UserDigitizedObjectPage',
        'inventory.UserDigitizedObjectTagIndexPage'
    ]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify('inventory')
        super().save(*args, **kwargs)


class UserDigitizedObject(Orderable):
    parent = ParentalKey(
        'inventory.UserDigitizedObjectInventoryPage',
        on_delete=models.PROTECT,
        related_name='itemized_digits'
    )
    digit = models.OneToOneField(
        'digitization.DigitizedObject',
        on_delete=models.CASCADE,
        related_name='user_associations'
    )

    @transaction.atomic
    def save(self, *args, **kwargs):
        creating = not self.pk
        super().save(*args, **kwargs)
        if creating:
            inventory_page = self.parent.specific
            digit_name = self.get_digit_name()
            new_page = UserDigitizedObjectPage(
                title=f"{digit_name}'s Details",
                user_digit=self,
                slug=slugify(digit_name)
            )
            inventory_page.add_child(instance=new_page)
            new_page.save_revision().publish()

    def get_digit_name(self):
        return self.digit.name

    def get_digit_description(self):
        return self.digit.description


class UserDigitizedObjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'inventory.UserDigitizedObjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class UserDigitizedObjectPage(Page):
    user_digit = models.OneToOneField(
        'inventory.UserDigitizedObject',
        on_delete=models.PROTECT,
        related_name='detail_page'
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
        index.SearchField('get_digit_description', partial_match=True, boost=1),
    ]

    parent_page_types = [
        'inventory.UserDigitizedObjectInventoryPage'
    ]

    subpage_types = [
        'inventory.UserDigitizedObjectTagIndexPage'
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('tags'),
            ],
            heading="Digit Metadata"
        ),
        FieldPanel('user_digit'),
        InlinePanel('digitized_object_images', label="Digit images"),
    ]

    def get_main_image(self):
        digit_item = self.digitized_object_images.first()
        if digit_item:
            return digit_item.image
        else:
            return None

    def get_detailed_digit_name(self):
        """Method to return the name of the digitized object."""
        return self.user_digit.get_digit_name()

    def get_detailed_digit_description(self):
        """Method to return the description of the digitized object."""
        return self.user_digit.get_digit_description()


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
