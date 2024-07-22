import uuid

from django.db import models
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
        link, created = InventoryLink.objects.get_or_create(tag=self)
        if created:
            return link
        return link

    def get_url(self):
        return reverse('link-tag', host='link', args=[str(self.uuid)])

    class Meta:
        verbose_name = "near field communication tag"
        verbose_name_plural = "near field communication tags"


class InventoryLink(models.Model):
    inventory = models.OneToOneField(
        "inventory.BaseInventory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    tag = models.OneToOneField(
        NearFieldCommunicationTag,
        on_delete=models.CASCADE,
        related_name='link'
    )

    def __str__(self):
        if self.inventory:
            return f"{self.tag} -> {self.inventory}"
        return str(self.tag)

    def get_url(self):
        if self.inventory:
            return self.inventory.url
        return None

    @property
    def url(self):
        return self.get_url()

    class Meta:
        verbose_name = "inventory link"
        verbose_name_plural = "inventory links"
        unique_together = ('inventory', 'tag')
        indexes = [
            models.Index(fields=['inventory']),
            models.Index(fields=['tag'])
        ]
