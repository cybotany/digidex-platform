import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_hosts.resolvers import reverse
from django.http import Http404

from base.utils import build_uri
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
        link = InventoryLink.objects.create(tag=self)
        return link

    def get_mapping_url(self):
        return reverse('link-tag', host='link', args=[str(self.uuid)])

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
    link = models.URLField(
        max_length=255,
        editable=True,
        null=True,
        blank=True
    )

    def get_url(self, user):
        if self.link:
            return self.link

        base_url = 'https://digidex.tech/inv'
        if self.tag.owner:
            owner = self.tag.owner
            owner_slug = slugify(owner.username)

            if user and user == owner:
                return f'{base_url}/{owner_slug}/ntag/{self.tag.uuid}'
            
            if self.asset:
                return f'{base_url}/{owner_slug}/{self.asset.slug}'

            return f'{base_url}/{owner_slug}'
        return base_url

    class Meta:
        verbose_name = "inventory link"
        verbose_name_plural = "inventory links"
        indexes = [
            models.Index(fields=['asset']),
            models.Index(fields=['tag'])
        ]
