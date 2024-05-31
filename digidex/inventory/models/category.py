import uuid
from django.db import models
from django.contrib import messages
from django.utils.text import slugify
from django.urls import reverse

from wagtail.models import Page


class Category(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category UUID"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category Slug"
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Category',
        help_text="Inventory Category Name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Inventory Category description."
    )
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.PROTECT,
        related_name="inventory_categories",
    )
    is_party = models.BooleanField(
        default=False,
        help_text="Indicates if this is the Party category."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.is_party:
            self.slug = slugify(self.name)
        else:
            self.name = 'Party'
            self.slug = 'party'
        super().save(*args, **kwargs)

    def add_digit(self, digit):
        DigitalObject = self.card_model
        itemized_digit, created = DigitalObject.objects.select_related('digit').get_or_create(
            category=self,
            digit=digit
        )
        if created:
            message = f"'{digit.name}' was created in the category '{self.name}'."
        else:
            message = f"'{digit.name}' already exists in the category '{self.name}'."

        messages.info(message)
        return itemized_digit

    def get_digit(self, digit):
        DigitalObject = self.card_model
        try:
            return self.itemized_digits.select_related('digit').get(digit=digit)
        except DigitalObject.DoesNotExist:
            return None

    def remove_digit(self, digit):
        itemized_digit = self.get_digit(digit)
        if itemized_digit:
            itemized_digit.delete()
            message = "Digit removed."
            messages.info(message)
        return itemized_digit

    def list_digits(self):
        return self.itemized_digits.select_related('digit')

    def get_panel_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'image_url': self.image_url,
            'delete_url': self.delete_url,
            'update_url': self.update_url
        }

    def get_card_details(self):
        return {
            'name': self.display_name,
            'description': self.display_description,
            'date': self.display_date,
            'page_url': self.page_url
        }

    @property
    def display_name(self):
        return self.name.title()

    @property
    def display_description(self):
        return self.description or 'No description available.'

    @property
    def display_date(self):
        return self.created_at.strftime('%b %d, %Y')

    @property
    def image_url(self):
        return None

    @property
    def parent_slug(self):
        return 'u'

    @property
    def base_slug(self):
        return slugify(self.name)

    @property
    def full_slug(self):
        return f'{self.parent_slug}/{self.base_slug}'

    @property
    def slug_kwargs(self):
        return self.user.slug_kwargs.update({'category_slug': self.slug})

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_inventory_category_page
            get_or_create_inventory_category_page(self)
        return self.page

    @property
    def page_url(self):
        return self.page.url

    @property
    def update_url(self):
        return reverse('inventory:update_category', kwargs=self.slug_kwargs)

    @property
    def delete_url(self):
        return reverse('inventory:delete_category', kwargs=self.slug_kwargs)

    @property
    def card_model(self):
        from inventory.models import DigitalObject
        return DigitalObject

    def __str__(self):
        return f"{self.display_name}'s Inventory Category"

    class Meta:
        unique_together = ('profile', 'name')


class CategoryPage(Page):
    heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    intro = models.TextField(
        null=True,
        blank=True
    )
    category = models.OneToOneField(
        Category,
        on_delete=models.PROTECT,
        related_name='page'
    )

    parent_page_types = [
        'inventory.UserProfilePage'
    ]

    @property
    def page_panel(self):
        return self.category.get_panel_details()

    @property
    def page_cards(self):
        card_list = []
        digits = self.category.list_digits()
        for digit in digits:
            card_list.append(digit.get_card_details())
        return card_list

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['category_panel'] = self.page_panel
        context['digit_cards'] = self.page_cards
        return context

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('category')

    class Meta:
        verbose_name = "Inventory Category Page"
