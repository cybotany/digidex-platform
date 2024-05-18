from django.apps import apps
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.fields import RichTextField

from digitization.models import DigitizedObjectInventory, DigitizedObject, DigitizedObjectJournalEntry


class UserInventory(Orderable, DigitizedObjectInventory):
    profile_page = ParentalKey(
        'profiles.UserProfilePage',
        on_delete=models.CASCADE,
        related_name='inventories'
    )
    detail_page = models.OneToOneField(
        'inventory.UserInventoryPage',
        on_delete=models.PROTECT,
        related_name='detailed_digit'
    )

    @property
    def profile(self):
        return self.profile_page.profile

    @property
    def user(self):
        return self.profile.user

    @property
    def username(self):
        return self.user.username

    @property
    def _username(self):
        return self.username.title()

    def save(self, *args, **kwargs):
        if not self.pk:
            user_inventories = UserInventory.objects.filter(profile_page=self.profile_page)
            count = user_inventories.count() + 1
            default_name = f"Box {count}"
            self.name = self.name or default_name
            self.slug = self.slug or slugify(self.name)
        
        original_slug = self.slug
        unique_slug = original_slug
        num = 1
        while UserInventory.objects.filter(profile_page=self.profile_page, slug=unique_slug).exclude(pk=self.pk).exists():
            unique_slug = f"{original_slug}-{num}"
            num += 1
        self.slug = unique_slug

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('profile_page', 'slug')


class UserInventoryPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True,
        help_text="Introduction text to display at the top of the index page."
    )
    inventory = models.OneToOneField(
        UserInventory,
        on_delete=models.PROTECT,
        related_name='inventory_page'
    )

    @property
    def profile_page(self):
        UserProfilePage = apps.get_model('profiles', 'UserProfilePage')
        parent = self.get_parent()
        if isinstance(parent.specific, UserProfilePage):
            return parent.specific
        return None

    @property
    def profile(self):
        return self.profile_page.profile

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        InlinePanel('itemized_digits', label="Itemized Digits"),
    ]

    parent_page_types = [
        'profiles.UserProfilePage'
    ]

    subpage_types = [
        'inventory.UserDigitPage'
    ]


class UserDigit(Orderable, DigitizedObject):
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


class JournalEntry(Orderable, DigitizedObjectJournalEntry):
    digit = models.OneToOneField(
        UserDigit,
        on_delete=models.CASCADE,
        related_name='journal_entries'
    )
    page = ParentalKey(
        UserDigitPage,
        on_delete=models.CASCADE,
        related_name='digit_journal_entries'
    )

    @property
    def digit_name(self):
        return self.digit.digit_name

    @property
    def digit_description(self):
        return self.digit.digit_description

    @property
    def image_caption(self):
        return self.caption

    @property
    def digit_inventory_page(self):
        return self.digit.page

    @property
    def digit_inventory_page_url(self):
        return self.digit_inventory_page.url

    @property
    def digit_detail_page(self):
        return self.digit.detail_page

    @property
    def digit_detail_page_url(self):
        return self.digit_detail_page.url
