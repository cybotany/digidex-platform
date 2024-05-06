from django.db import models
from django.utils.text import slugify
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class UserDigitizedObjectInventoryPage(Page):
    intro = models.TextField(
        blank=True,
        help_text="Introduction text to display at the top of the index page."
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    parent_page_types = [
        'accounts.UserProfilePage'
    ]

    subpage_types = [
        'inventory.UserDigitizedObjectPage'
    ]


class UserDigitizedObject(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='user_digits'
    )
    digit = models.OneToOneField(
        'digitization.DigitizedObject',
        on_delete=models.CASCADE,
        related_name='user_association'
    )

    def get_digit_name(self):
        return self.digit.name

    def get_digit_description(self):
        return self.digit.description

    def create_digit_page(self):
        inventory_page = UserDigitizedObjectInventoryPage.objects.filter(owner=self.user).first()
        
        if not inventory_page:
            return None
        
        user_digit_page = UserDigitizedObjectPage(
            title=f"Digitized Object: {self.get_digit_name()}",
            owner=self.user,
            slug=slugify(self.digit.name),
            user_digit=self
        )
        inventory_page.add_child(instance=user_digit_page)  
        user_digit_page.save_revision().publish()


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
        index.SearchField('get_digit_name', partial_match=True, boost=2),
        index.SearchField('get_digit_description', partial_match=True, boost=1),
    ]

    parent_page_types = [
        'inventory.UserDigitizedObjectInventoryPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user_digit')
    ]

    def get_digit_name(self):
        """Method to return the name of the digitized object."""
        return self.user_digit.get_digit_name()

    def get_digit_description(self):
        """Method to return the description of the digitized object."""
        return self.user_digit.get_digit_description()
