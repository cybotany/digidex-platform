import uuid
from django.db import models
from django.apps import apps
from django.utils.text import slugify
from django.urls import reverse

from wagtail.models import Page


class InventoryDigit(models.Model):
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

    def save(self, *args, **kwargs):
        self.slug = self.create_unique_slug()
        super().save(*args, **kwargs)

    def create_unique_slug(self):
        base_slug = slugify(self.name) if self.name else 'digit'
        slug = base_slug
        counter = 1

        parent_page = self._parent_page
        if parent_page:
            while InventoryDigitPage.objects.filter(slug=slug, path__startswith=parent_page.path).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
        return slug

    def create_page(self):
        slug = self.create_unique_slug()
        digit_page = InventoryDigitPage(
            title=self.name,
            slug=slug,
            owner=self.user,
            heading=self.name,
            intro=self.description,
            digit=self,
        )
        parent_page = self._parent_page
        if parent_page:
            parent_page.add_child(instance=digit_page)
            digit_page.save_revision().publish()
        return digit_page

    def create_journal(self):
        journal = apps.get_model('journal', 'EntryCollection').objects.create(
            digit=self
        )
        return journal

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

        super().delete(*args, **kwargs)
    
    @property
    def _user(self):
        return self.category.user if self.category else None

    @property
    def _parent_page(self):
        return self.category.page if self.category else None

    @property
    def _name(self):
        return self.digit.name if self.digit else None

    @property
    def _description(self):
        return self.digit.description if self.digit else None

    @property
    def _date(self):
        return self.digit.created_at if self.digit else None

    @property
    def _image_url(self):
        return None

    @property
    def _page(self):
        return self.page if hasattr(self, 'page') else None

    @property
    def _page_url(self):
        return self._page.url if self._page else '#'

    @property
    def _update_url(self):
        return reverse('inventory:update_digit', kwargs={'digit_uuid': self.uuid})

    @property
    def _delete_url(self):
        return reverse('inventory:delete_digit', kwargs={'digit_uuid': self.uuid})

    @property
    def digit_panel(self):
        return self.get_panel_details()

    @property
    def journal_cards(self):
        card_details_list = []
        notes = [] # self.list_notes()
        for note in notes:
            card_details_list.append(note.get_card_details())
        return card_details_list

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    def __str__(self):
        return self.name.title() if self.name else 'Unnamed'

    class Meta:
        unique_together = ('category', 'digit')


class InventoryDigitPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = models.TextField(
        blank=True
    )
    digit = models.OneToOneField(
        InventoryDigit,
        on_delete=models.PROTECT,
        related_name='page'
    )

    parent_page_types = [
        'inventory.InventoryCategoryPage',
    ]

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['digit_panel'] = self.digit.digit_panel
        context['journal_cards'] = self.digit.journal_cards
        return context