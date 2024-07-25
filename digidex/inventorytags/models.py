import uuid

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_hosts.resolvers import reverse
from django.http import Http404, HttpResponse

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
        # Check if link already exists
        link = self.get_link()
        if not link:
            link = InventoryLink.objects.create(tag=self)
        return link

    def get_link(self):
        try:
            link = InventoryLink.objects.get(tag=self)
            return link
        except InventoryLink.DoesNotExist:
            return None

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

    def get_linked_url(self):
        if not self.active:
            return HttpResponse("This tag is not active.", status=403)
        tag_link = self.get_link()
        if tag_link and tag_link.inventory:
            return tag_link.get_inventory_url()
        return self.get_owner_url()

    class Meta:
        verbose_name = "near field communication tag"
        verbose_name_plural = "near field communication tags"


class InventoryLink(models.Model):
    inventory = models.OneToOneField(
        "inventory.BaseInventory",
        on_delete=models.SET_NULL,
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

    def get_inventory_url(self):
        if self.inventory:
            return build_uri(self.inventory.slug)
        return None

    class Meta:
        verbose_name = "inventory link"
        verbose_name_plural = "inventory links"
        unique_together = ('inventory', 'tag')
        indexes = [
            models.Index(fields=['inventory']),
            models.Index(fields=['tag'])
        ]
