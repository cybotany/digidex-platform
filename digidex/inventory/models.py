import uuid
from django.db import models
from django.contrib import messages
from django.conf import settings
from django.utils.text import slugify

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class Category(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Category UUID"
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
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="Inventory Category Slug"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
            original_name = self.name
            unique_name = original_name
            num = 1
            while Category.objects.filter(user=self.user, name=unique_name).exclude(pk=self.pk).exists():
                unique_name = f"{original_name} ({num})"
                num += 1
            self.name = unique_name
            self.slug = f"inv/{slugify(self.name)}"
        super().save(*args, **kwargs)

    def list_digits(self):
        return self.itemized_digits.prefetch_related('digit').all()

    def add_digit(self, digit):
        itemized_digit, created = ItemizedDigit.objects.select_related('digit').get_or_create(
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
        return self.itemized_digits.select_related('digit').get(digit=digit)

    def remove_digit(self, digit):
        itemized_digit = self.get_digit(digit)
        itemized_digit.delete()
        message = f"'{digit.name}' was removed from the category '{self.name}'."
        messages.info(message)
        return itemized_digit

    class Meta:
        unique_together = ('user', 'name')


class ItemizedDigit(models.Model):
    category = models.ForeignKey(
        'inventory.Category',
        on_delete=models.CASCADE,
        related_name='itemized_digits'
    )
    digit = models.OneToOneField(
        'digitization.DigitalObject',
        on_delete=models.CASCADE,
        related_name='inventory_category'
    )

    @property
    def name(self):
        return self.digit.name

    @property
    def description(self):
        return self.digit.description

    @property
    def created_at(self):
        return self.digit.created_at

    @property
    def last_modified(self):
        return self.digit.last_modified

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    class Meta:
        unique_together = ('category', 'digit')


class CategoryPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True
    )
    category = models.OneToOneField(
        Category,
        on_delete=models.PROTECT,
        related_name='page'
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['itemized_digits'] = self.category.list_digits()
        return context

    parent_page_types = [
        'accounts.UserPage'
    ]

    subpage_types = [
        'digitization.DigitalObjectPage'
    ]

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('category')
