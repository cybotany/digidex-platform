import uuid
from django.db import models
from django.template.defaultfilters import slugify


class DigitizedObjectInventory(models.Model):
    """
    Base class for digitized object inventories, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object inventory.
        uuid (UUIDField): The unique identifier for the digitized object inventory.
        slug (SlugField): The unique slug for the digitized object inventory.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='Inventory',
        help_text="Digitized Object Inventory name."
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255,
        verbose_name="Digitized Object Inventory Slug"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True



class DigitizedObject(models.Model):
    """
    Base class for digitized objects, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object.
        uuid (UUIDField): The unique identifier for the digitized object.
        description (TextField): A detailed description of the digitized object.
        created_at (DateTimeField): The date and time the digitized object was created.
        last_modified (DateTimeField): The date and time the digitized object was last modified.
    """
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class DigitizedObjectJournalEntry(models.Model):
    digit = models.ForeignKey(
        DigitizedObject,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
        help_text="Digitized object image."
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Image caption."
    )

    class Meta:
        abstract = True
