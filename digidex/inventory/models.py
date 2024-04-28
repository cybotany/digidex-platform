import uuid

from django.utils.text import slugify
from django.db import models
from django.conf import settings

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.search import index

from nfc.models import NearFieldCommunicationTag


class UserIndexPage(Page):
    body = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    subpage_types = ['inventory.UserPage']


class UserPage(Page):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="user_pages"
    )
    avatar = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    biography = RichTextField(
        blank=True,
        null=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_username', partial_match=True, boost=2),
        index.SearchField('biography'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('avatar'),
        FieldPanel('biography')
    ]

    subpage_types = ['inventory.DigitPage']

    def get_username(self):
        """Method to return the username of the associated user."""
        return self.user.username

    class Meta:
        verbose_name = "User Page"


class Digit(Orderable):
    page = ParentalKey(
        'UserPage',
        null=True,
        on_delete=models.CASCADE,
        related_name='digits'
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False
    )
    slug = models.SlugField(
        null=True,
        db_index=True,
        verbose_name="Digit Slug"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID"
    )
    ntag = models.OneToOneField(
        NearFieldCommunicationTag,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='digit'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified"
    )


    def save(self, *args, **kwargs):
        if not self.pk:
            # Create a unique slug for the digit within the scope of the user
            self.slug = slugify(self.name)
            original_slug = self.slug
            count = 1

            while Digit.objects.filter(page=self.page, slug=self.slug).exists():
                self.slug = f'{original_slug}-{count}'
                count += 1

        super(Digit, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class DigitPage(Page):
    digit = models.ForeignKey(
        Digit,
        on_delete=models.PROTECT,
        related_name='pages'
    )
    user = models.ForeignKey(
        UserPage,
        on_delete=models.PROTECT,
        related_name='digit_pages'
    )
    description = RichTextField(
        blank=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('get_digit_name', partial_match=True, boost=2),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('digit'),
        PageChooserPanel('user'),
        FieldPanel('description'),
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
        return self.digit.name

    def save(self, *args, **kwargs):
        if not self.pk:
            base_slug = slugify(self.digit.name)
            self.slug = base_slug
            count = 1

            while DigitPage.objects.filter(slug=self.slug, user=self.user).exists():
                self.slug = f'{base_slug}-{count}'
                count += 1

        super(DigitPage, self).save(*args, **kwargs)


class DigitPageGalleryImage(Orderable):
    page = ParentalKey(
        DigitPage,
        on_delete=models.CASCADE,
        related_name='digit_images'
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
