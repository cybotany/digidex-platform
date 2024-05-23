import uuid
from django.apps import apps
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.fields import RichTextField


class DigitalObjectPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    digital_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    search_fields = Page.search_fields + [
        index.SearchField('heading', partial_match=True, boost=2)
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]


class DigitalObject(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized object name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Digitized object description."
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="Digitized Object Slug"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def digit_name(self):
        return self.name.title()

    @property
    def digit_description(self):
        if self.description:
            return self.description
        return "No description available."

    @property
    def page(self):
        try:
            return DigitalObjectPage.objects.get(
                content_type=ContentType.objects.get_for_model(self),
                object_id=self.pk
            )
        except DigitalObjectPage.DoesNotExist:
            raise ObjectDoesNotExist("There's no page for this digitized object.")

    class Meta:
        abstract = True


class DigitalPartyObject(DigitalObject):
    party = models.ForeignKey(
        'party.UserParty',
        on_delete=models.CASCADE,
        related_name='party_digits'
    )
    
    def create_digit_page(self):
        user_profile_page = self.party.profile_page
        try:
            if self.page:
                pass
        except ObjectDoesNotExist:
            base_slug = slugify(self.digit_name)
            unique_slug = base_slug
            counter = 1
           
            while Page.objects.filter(slug=unique_slug, path__startswith=self.get_parent().path).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            user_digit_page = DigitalObjectPage(
                title={self.digit_name},
                owner=self.user,
                slug=unique_slug,
                heading=self.digit_name,
                intro=self.digit_description
            )
            user_profile_page.page.add_child(instance=user_digit_page)
            user_digit_page.save_revision().publish()

            self.detail_page = user_digit_page
            self.save() 
        return self.detail_page


class DigitalInventoryObject(DigitalObject):
    inventory = models.ForeignKey(
        'inventory.UserInventory',
        on_delete=models.CASCADE,
        related_name='itemized_digits'
    )

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()

    def create_digit_page(self):
        user_inventory_page = self.inventory.page
        if not user_inventory_page:
            raise ObjectDoesNotExist("There's no inventory page to create the digit page under.")
        try:
            if self.detail_page:
                pass
        except ObjectDoesNotExist:
            base_slug = slugify(self.digit_name)
            unique_slug = base_slug
            counter = 1
           
            while Page.objects.filter(slug=unique_slug, path__startswith=self.get_parent().path).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            user_digit_page = DigitalObjectPage(
                title={self.digit_name},
                owner=self.user,
                slug=unique_slug,
                heading=self.digit_name,
                intro=self.digit_description
            )
            self.page.add_child(instance=user_digit_page)
            user_digit_page.save_revision().publish()

            self.detail_page = user_digit_page
            self.save() 
        return self.detail_page

    def __str__(self):
        return f"{self.digit_name}"
