import uuid
from django.db import models
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from django.urls import reverse

from wagtail.models import Page


class DigitalObject(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        help_text="Digitized object name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Digitized object description."
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="digits",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def digit_name(self):
        return self.name.title()

    @property
    def digit_description(self):
        if self.description:
            return self.description
        return "No description available."

    @property
    def digit_page(self):
        try:
            return DigitalObjectPage.objects.select_related('digit').get(
                digit=self
            )
        except DigitalObjectPage.DoesNotExist:
            raise ObjectDoesNotExist("There's no page for this digitized object.")

    def create_unique_slug(self, parent_page, base_slug):
        slug = base_slug
        counter = 1
        while DigitalObjectPage.objects.filter(slug=slug, path__startswith=parent_page.path).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def create_digit_page(self, parent_page):
        base_slug = slugify(self.name)
        unique_slug = self.create_unique_slug(parent_page, base_slug)
        digitized_object_page = DigitalObjectPage(
            title=self.name,
            slug=unique_slug,
            owner=self.user,
            digit=self,
        )
        parent_page.add_child(instance=digitized_object_page)
        digitized_object_page.save_revision().publish()
        return digitized_object_page

    def create_journal(self):
        journal = apps.get_model('journal', 'EntryCollection').objects.create(
            digit=self
        )
        return journal

    def get_journal_entries(self):
        try:
            journal_collection = self.journal
            if journal_collection:
                return journal_collection.get_all_entries().select_related('journal').prefetch_related('digit')
        except ObjectDoesNotExist:
            return None

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
            digital_object_page = DigitalObjectPage.objects.get(digit=self)
            digital_object_page.delete()
        except DigitalObjectPage.DoesNotExist:
            pass

    def __str__(self):
        return f"{self.digit_name}"


class DigitalObjectPage(Page):
    digit = models.ForeignKey(
        'digitization.DigitalObject',
        on_delete=models.PROTECT,
        related_name='page'
    )

    @property
    def delete_url(self):
        return reverse('inventory:delete_digit', kwargs={'digit_uuid': self.digit.uuid})

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['journal_entries'] = self.digit.get_journal_entries().prefetch_related('related_model')
        return context

    @classmethod
    def get_queryset(cls):
        return super().get_queryset().select_related('digit')
