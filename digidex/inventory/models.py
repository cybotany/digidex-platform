import uuid
from django.db import models
from django.contrib import messages
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
            self.name = self.create_unique_name()
            self.slug = self.create_unique_slug()
        super().save(*args, **kwargs)

    @property
    def parent_page(self):
        return self.user.page

    def create_unique_name(self):
        base_name = self.name
        name = base_name
        counter = 1

        while Category.objects.filter(user=self.user, name=name).exists():
            name = f"{base_name} {counter}"
            counter += 1
        return name

    def create_unique_slug(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1

        parent_page = self.parent_page

        while InventoryCategoryPage.objects.filter(parent=parent_page, slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def create_page(self):
        self.slug = self.create_unique_slug()
        category_page = InventoryCategoryPage(
            title=self.name,
            slug=self.slug,
            owner=self.user,
            heading=self.name,
            intro=self.description,
            category=self,
        )
        self.parent_page.add_child(instance=category_page)
        category_page.save_revision().publish()
        return category_page

    def list_digits(self):
        return self.itemized_digits.select_related('digit').all()

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

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')


class InventoryCategoryPage(Page):
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

    parent_page_types = [
        'accounts.UserPage'
    ]

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('category')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['itemized_digits'] = self.category.list_digits()
        return context


class ItemizedDigit(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Digit UUID"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Inventory Digit Slug"
    )
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

    @property
    def user(self):
        return self.category.user

    @property
    def parent_page(self):
        return self.category.page

    def save(self, *args, **kwargs):
        self.slug = self.create_unique_slug()
        super().save(*args, **kwargs)

    def create_unique_slug(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1

        parent_page = self.parent_page

        while ItemizedDigitPage.objects.filter(parent=parent_page, slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def create_page(self):
        slug = self.create_unique_slug()
        category_page = ItemizedDigitPage(
            title=self.name,
            slug=slug,
            owner=self.user,
            heading=self.name,
            intro=self.description,
            digit=self,
        )
        self.parent_page.add_child(instance=category_page)
        category_page.save_revision().publish()
        return category_page

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    def __str__(self):
        return self.name.title()

    class Meta:
        unique_together = ('category', 'digit')


class ItemizedDigitPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True
    )
    digit = models.ForeignKey(
        ItemizedDigit,
        on_delete=models.PROTECT,
        related_name='page'
    )

    parent_page_types = [
        'inventory.InventoryCategoryPage',
    ]

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    @property
    def delete_url(self):
        return reverse('inventory:delete_digit', kwargs={'digit_uuid': self.digit.uuid})

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['journal_entries'] = self.digit.get_journal_entries().prefetch_related('related_model')
        return context

