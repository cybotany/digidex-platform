import uuid
from django.db import models
from django.apps import apps
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
    digital_object = models.ForeignKey(
        'digitization.DigitalObject',
        on_delete=models.PROTECT,
        related_name='page'
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
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(
        db_index=True
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
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
    def digit_page(self):
        try:
            return DigitalObjectPage.objects.get(
                digital_object=self
            )
        except DigitalObjectPage.DoesNotExist:
            raise ObjectDoesNotExist("There's no page for this digitized object.")

    def create_digit_page(self):
        parent_page = None
        if isinstance(self.content_object, apps.get_model('parties', 'UserParty')):
            parent_page = self.content_object.user.profile.page
        elif isinstance(self.content_object, apps.get_model('inventory', 'UserInventory')):
            parent_page = self.content_object.page

        if not parent_page:
            raise ObjectDoesNotExist("There's no parent page to create the digit page under.")

        try:
            if self.digit_page:
                pass
        except ObjectDoesNotExist:
            base_slug = slugify(self.digit_name)
            unique_slug = base_slug
            counter = 1

            while Page.objects.filter(slug=unique_slug, path__startswith=parent_page.path).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            user_digit_page = DigitalObjectPage(
                title=self.digit_name,
                owner=self.content_object.user,
                slug=unique_slug,
                heading=self.digit_name,
                intro=self.digit_description
            )
            parent_page.add_child(instance=user_digit_page)
            user_digit_page.save_revision().publish()

            self.detail_page = user_digit_page
            self.save()
        return self.detail_page

    def __str__(self):
        return f"{self.digit_name}"
