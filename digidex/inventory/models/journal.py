import uuid
from django.db import models

from base.utils.storage import PublicMediaStorage


def journal_image_path(instance, filename):
    detail_page = instance.page
    owner = detail_page.owner
    if detail_page.specific_class.__name__ == 'InventoryCategoryPage':
        subdirectory = 'categories'
    else:
        subdirectory = 'objects'
    extension = filename.split('.')[-1]
    return f'users/{owner.uuid}/{subdirectory}/{detail_page.id}/{uuid.uuid4()}.{extension}'

class JournalEntry(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Journal Entry Collection UUID"
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Image caption."
    )
    note = models.TextField(
        blank=True,
        null=True,
        help_text="Journal entry note."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Journal entry made on{self.created_at}."

    class Meta:
        abstract = True
