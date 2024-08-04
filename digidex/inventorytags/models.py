import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_hosts.resolvers import reverse

from inventorytags.validators import validate_serial_number


class NearFieldCommunicationTag(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    serial_number = models.CharField(
        max_length=32,
        editable=False,
        unique=True,
        db_index=True,
        validators=[validate_serial_number]
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )
    active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"NFC Tag: {self.serial_number}"

    def activate_tag(self):
        self.active = True
        self.save()

    def deactivate_tag(self):
        self.active = False
        self.save()

    def create_link(self):
        from inventorytags.models import InventoryLink
        if hasattr(self, 'link'):
            raise ValueError("An InventoryLink already exists for this tag.")
        link = InventoryLink.objects.create(tag=self)
        return link

    def get_mapping_url(self):
        return reverse('link-tag', host='default', args=[str(self.uuid)])

    class Meta:
        verbose_name = "near field communication tag"
        verbose_name_plural = "near field communication tags"


class InventoryLink(models.Model):
    asset = models.ForeignKey(
        'inventory.InventoryAssetPage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )
    tag = models.OneToOneField(
        NearFieldCommunicationTag,
        on_delete=models.CASCADE,
        related_name='link'
    )
    url = models.URLField(
        max_length=255,
        editable=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "inventory link"
        verbose_name_plural = "inventory links"
        indexes = [
            models.Index(fields=['asset']),
            models.Index(fields=['tag'])
        ]
