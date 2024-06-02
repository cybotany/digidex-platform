import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

from wagtail.models import Page

from inventory.utils import get_or_create_inventory_category_page


class DigitalObject(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object Slug"
    )
    category = models.ForeignKey(
        'inventory.Category',
        on_delete=models.CASCADE,
        related_name='itemized_digits'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="digital_objects",
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized Object Name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Digitized Object Description."
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
        if hasattr(self, 'page'):
            self.page.delete()
        if hasattr(self, 'journal'):
            self.journal.delete()
        super().delete(*args, **kwargs)

    def create_journal(self):
        if hasattr(self, 'journal'):
            return self.journal
        EntryCollection = self.card_model
        return EntryCollection.objects.create(digital_object=self)

    def create_page(self):
        if not DigitalObjectPage.objects.filter(digital_object=self).exists():
            digit_page = DigitalObjectPage(
                title=self.name,
                slug=self.base_slug,
                owner=self.user,
                digital_object=self
            )

            parent_page = get_or_create_inventory_category_page(self.category)
            parent_page.add_child(instance=digit_page)
            digit_page.save_revision().publish()
        else:
            digit_page = DigitalObjectPage.objects.get(digital_object=self)
        return digit_page

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
        if self.description:
            return self.description
        return "No description available."
    
    @property
    def display_date(self):
        return self.created_at

    @property
    def image_url(self):
        return None

    @property
    def parent_slug(self):
        return self.category.full_slug

    @property
    def base_slug(self):
        return slugify(self.name)

    @property
    def full_slug(self):
        return f'{self.parent_slug}/{self.base_slug}'

    @property
    def slug_kwargs(self):
        base_kwargs = self.category.slug_kwargs
        base_kwargs['digit_slug'] = self.base_slug
        return base_kwargs

    @property
    def _page(self):
        if hasattr(self, 'page'):
            return self.page
        return self.create_page()

    @property
    def page_url(self):
        return self._page.url if self._page else '#'

    @property
    def update_url(self):
        return reverse('inventory:update_digit', kwargs=self.slug_kwargs)

    @property
    def delete_url(self):
        return reverse('inventory:delete_digit', kwargs=self.slug_kwargs)

    @property
    def card_model(self):
        from inventory.models.journal import EntryCollection
        return EntryCollection

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('category')

    def __str__(self):
        return self.display_name

    class Meta:
        unique_together = ('category', 'name')


class DigitalObjectPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True
    )
    digital_object = models.OneToOneField(
        'inventory.DigitalObject',
        on_delete=models.PROTECT,
        related_name='page'
    )

    parent_page_types = [
        'inventory.CategoryPage',
    ]

    def delete(self, *args, **kwargs):
        if hasattr(self, 'page'):
            self.page.delete()
        super().delete(*args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['digit_panel'] = self.page_panel
        context['journal_cards'] = self.page_cards
        return context

    @property
    def page_panel(self):
        return self.digital_object.get_panel_details()

    @property
    def page_cards(self):
        card_list = []
        entries = self.digital_object.journal.list_entries()
        for entry in entries:
            card_list.append(entry.get_card_details())
        return card_list

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('journal')
