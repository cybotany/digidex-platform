import uuid
from django.db import models
from django.apps import apps
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
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        db_index=True
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
    def digit_page(self):
        try:
            return InventoryPage.objects.select_related('digit').get(
                digit=self
            )
        except InventoryPage.DoesNotExist:
            raise InventoryPage("There's no page for this digitized object.")

    def create_unique_slug(self):
        category_slug = slugify(self.category.name)
        digit_slug = slugify(self.name)
        
        slug = f"{category_slug}/{digit_slug}"
        counter = 1

        while InventoryPage.objects.filter(slug=slug, path__startswith=category_slug.path).exists():
            slug = f"{slug}-{counter}"
            counter += 1
        return slug

    def create_digit_page(self):
        parent_page = self.category.page
        unique_slug = self.create_unique_slug()
        digit_page = InventoryPage(
            title=self.name,
            slug=unique_slug,
            owner=self.user,
            digit=self,
        )
        parent_page.add_child(instance=digit_page)
        digit_page.save_revision().publish()
        return digit_page

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    def delete(self, *args, **kwargs):
        related_models = [
            ('journal', 'EntryCollection'),
            ('nfc', 'NearFieldCommunicationTag'),
        ]

        for app_label, model_name in related_models:
            model = apps.get_model(app_label, model_name)
            related_objects = model.objects.filter(digit=self)
            for obj in related_objects:
                obj.delete()

        try:
            digital_object_page = InventoryPage.objects.get(digit=self)
            digital_object_page.delete()
        except InventoryPage.DoesNotExist:
            pass

    def __str__(self):
        return f"{self.digit_name}"

    class Meta:
        unique_together = ('category', 'digit')


class InventoryPage(Page):
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
        'accounts.UserPage'
    ]

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    @property
    def delete_url(self):
        return reverse('inventory:delete_digit', kwargs={'digit_uuid': self.digit.uuid})

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['itemized_digits'] = self.category.list_digits()
        context['journal_entries'] = self.digit.get_journal_entries().prefetch_related('related_model')
        return context
