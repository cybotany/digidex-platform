import uuid
from django.db import models
from django.contrib import messages
from django.utils.text import slugify
from django.urls import reverse
\
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
    user_profile = models.ForeignKey(
        'inventory.UserProfile',
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
        InventoryDigit = self._card_model
        itemized_digit, created = InventoryDigit.objects.select_related('digit').get_or_create(
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
        InventoryDigit = self._card_model
        try:
            return self.itemized_digits.select_related('digit').get(digit=digit)
        except InventoryDigit.DoesNotExist:
            return None

    def remove_digit(self, digit):
        itemized_digit = self.get_digit(digit)
        if itemized_digit:
            itemized_digit.delete()
            message = f"'{digit.name}' was removed from the category '{self.name}'."
            messages.info(message)
        return itemized_digit

    def list_digits(self):
        return self.itemized_digits.select_related('digit')

    def get_panel_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'image_url': self._image_url,
            'delete_url': self._delete_url,
            'update_url': self._update_url
        }

    def get_card_details(self):
        return {
            'name': self._name,
            'description': self._description,
            'date': self._date,
            'page_url': self._page_url
        }

    @property
    def _name(self):
        return self.name.title()

    @property
    def _description(self):
        return self.description or 'No description available.'

    @property
    def _date(self):
        return self.created_at.strftime('%b %d, %Y')

    @property
    def _image_url(self):
        return None

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_inventory_category_page
            get_or_create_inventory_category_page(self)
        return self.page

    @property
    def _page_url(self):
        return self._page.url

    @property
    def _update_url(self):
        return reverse('inventory:update_category', kwargs={'category_slug': self.slug})

    @property
    def _delete_url(self):
        return reverse('inventory:delete_category', kwargs={'category_slug': self.slug})

    @property
    def _card_model(self):
        from inventory.models import InventoryDigit
        return InventoryDigit

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user_profile', 'name')


class InventoryCategoryPage(Page):
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

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('category')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['category_panel'] = self.page_panel
        context['digit_cards'] = self.page_cards
        return context
