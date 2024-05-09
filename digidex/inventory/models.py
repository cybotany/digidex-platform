from django.apps import apps
from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

from digitization.models import DigitizedObject, DigitizedObjectImage


class UserDigitizedObjectInventoryPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True,
        help_text="Introduction text to display at the top of the index page."
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
        InlinePanel('user_digitized_objects', label="Digitized Objects"),
    ]

    parent_page_types = [
        'profiles.UserProfilePage'
    ]

    subpage_types = [
        'inventory.UserDigitizedObjectPage'
    ]


class UserDigitizedObject(Orderable, DigitizedObject):
    page = ParentalKey(
        UserDigitizedObjectInventoryPage,
        on_delete=models.CASCADE,
        related_name='user_digitized_objects'
    )
    user_profile = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name='user_digits'
    )

    @property
    def user(self):
        return self.user_profile.user

    @property
    def username(self):
        return self.user.username

    @property
    def digit_description(self):
        return self.digit.description

    @property
    def digit_name(self):
        return self.digit.name

    @property
    def digit_description(self):
        return self.digit.description

    def create_digit_page(self):
        inventory_page = UserDigitizedObjectInventoryPage.objects.filter(owner=self.user).first()

        if not inventory_page:
            return None

        user_digit_page = UserDigitizedObjectPage(
            title=f"Digitized Object: {self.digit_name}",
            owner=self.user,
            slug=slugify(self.digit_name),
            user_digit=self
        )
        inventory_page.add_child(instance=user_digit_page)
        user_digit_page.save_revision().publish()
        return user_digit_page

    def __str__(self):
        return f"{self.name}"

    def get_associated_page_url(self):
        try:
            user_digit_page = self.detail_page
            return user_digit_page.url if user_digit_page else None
        except UserDigitizedObject.DoesNotExist:
            return None
        except UserDigitizedObjectPage.DoesNotExist:
            return None


class UserDigitizedObjectImage(Orderable, DigitizedObjectImage):
    digit = ParentalKey(
        UserDigitizedObject,
        on_delete=models.CASCADE,
        related_name='images'
    )
    
    @property
    def digit_name(self):
        return self.digit.name
    
    @property
    def digit_description(self):
        return self.digit.description
    
    @property
    def image_caption(self):
        return self.caption


class UserDigitizedObjectPage(Page):
    user_digit = models.OneToOneField(
        'inventory.UserDigitizedObject',
        on_delete=models.PROTECT,
        related_name='detail_page'
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
        index.SearchField('digit_name', partial_match=True, boost=2),
        index.SearchField('digit_description', partial_match=True, boost=1),
    ]

    parent_page_types = [
        'inventory.UserDigitizedObjectInventoryPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user_digit')
    ]

    @property
    def digit_name(self):
        """Method to return the name of the digitized object."""
        return self.user_digit.digit_name

    @property
    def digit_description(self):
        """Method to return the description of the digitized object."""
        return self.user_digit.digit_description
