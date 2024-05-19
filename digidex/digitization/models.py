import uuid
from django.apps import apps
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.fields import RichTextField


class UserDigit(Orderable):
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
    page = ParentalKey(
        UserInventoryPage,
        on_delete=models.CASCADE,
        related_name='itemized_digits'
    )
    user_profile = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name='user_digits'
    )
    detail_page = models.OneToOneField(
        'inventory.UserDigitPage',
        on_delete=models.PROTECT,
        related_name='detailed_digit'
    )

    @property
    def user(self):
        return self.user_profile.user

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()

    @property
    def digit_description(self):
        return self.description

    @property
    def digit_name(self):
        return self.name.title()

    def create_digit_page(self):
        inventory_page = UserInventoryPage.objects.filter(owner=self.user).first()
        if not inventory_page:
            raise ObjectDoesNotExist("User has no inventory page.")
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

            user_digit_page = UserDigitPage(
                title={self.digit_name},
                owner=self.user,
                slug=unique_slug,
                heading=self.digit_name,
                intro=self.digit_description
            )
            inventory_page.add_child(instance=user_digit_page)
            user_digit_page.save_revision().publish()

            self.page = inventory_page
            self.detail_page = user_digit_page
            self.save() 
        return self.detail_page

    def __str__(self):
        return f"{self.digit_name}"


class UserDigitPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('digit_name', partial_match=True, boost=2),
        index.SearchField('digit_description', partial_match=True, boost=1),
    ]

    parent_page_types = [
        'inventory.UserInventoryPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    @property
    def digit_name(self):
        """Method to return the name of the digitized object."""
        return self.detailed_digit.digit_name

    @property
    def digit_description(self):
        """Method to return the description of the digitized object."""
        return self.detailed_digit.digit_description
