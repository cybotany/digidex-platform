import uuid
from django.db import models
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


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

    def __str__(self):
        return f"{self.digit_name}"
