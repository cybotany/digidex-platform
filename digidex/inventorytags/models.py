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
    link = models.URLField(
        max_length=255,
        editable=True,
        blank=True,
        null=True
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

    def get_mapping_url(self):
        return reverse('link-tag', host='link', args=[str(self.uuid)])

    def get_owner_url(self):
        from inventory.models import UserInventoryIndex
        user_slug = slugify(self.owner.username)
        try:
            user_inventory = UserInventoryIndex.objects.get(slug=user_slug)
            return build_uri(user_inventory.slug)
        except UserInventoryIndex.DoesNotExist:
            raise Http404('Owner page not found')

    class Meta:
        verbose_name = "near field communication tag"
        verbose_name_plural = "near field communication tags"
