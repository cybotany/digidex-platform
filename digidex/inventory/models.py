import uuid

from django.db import models
from django.conf import settings

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel
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


class Digit(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID"
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
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
        related_name='digits'
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
    ]

    def get_digit_name(self):
        """Method to return the name of the digitized object."""
        return self.digit.name
