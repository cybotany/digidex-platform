import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings  
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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
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
        if not self.slug:
            self.slug = self.full_slug
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.itemized_digits.exists():
            raise ValidationError(
                f"Cannot delete category '{self.name}' because it contains digitized objects. "
                "Please move or delete all digitized objects first."
            )
        if hasattr(self, 'page'):
            self.page.delete()
        super().delete(*args, **kwargs)

    def add_digit(self, digit):
        DigitalObject = self.card_model
        if DigitalObject.objects.filter(category=self, digit=digit).exists():
            raise ValidationError(
                f"'{digit.name}' already exists in the category '{self.name}'."
            )

        itemized_digit = DigitalObject.objects.create(
            category=self,
            digit=digit
        )
        return itemized_digit

    def get_digit(self, digit):
        DigitalObject = self.card_model
        try:
            return self.itemized_digits.select_related('digit').get(digit=digit)
        except DigitalObject.DoesNotExist:
            raise ValidationError(
                f"The digit '{digit.name}' does not exist in the category '{self.name}'."
            )

    def remove_digit(self, digit):
        itemized_digit = self.get_digit(digit)
        if itemized_digit:
            itemized_digit.delete()
            return itemized_digit
        else:
            raise ValidationError(
                f"The digit '{digit.name}' does not exist in the category '{self.name}'."
            )

    def list_digits(self):
        return self.itemized_digits.select_related('category')

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
        return self.user.full_slug

    @property
    def base_slug(self):
        if self.is_party:
            return 'party'
        return slugify(self.name)

    @property
    def full_slug(self):
        return f'{self.parent_slug}/{self.base_slug}'

    @property
    def slug_kwargs(self):
        base_kwargs = self.user.slug_kwargs
        base_kwargs['category_slug'] = self.base_slug
        return base_kwargs

    @property
    def _page(self):
        if not hasattr(self, 'page'):
            from inventory.utils import get_or_create_inventory_category_page
            get_or_create_inventory_category_page(self)
        return self.page

    @property
    def page_url(self):
        return self._page.url

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
        return f"Inventory Category {self.display_name}"

    class Meta:
        unique_together = ('user', 'name')


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
