import uuid

from django.db import models, transaction
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.models import Orderable

from inventory.validators import validate_serial_number


class NearFieldCommunicationTag(ClusterableModel):
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
    type = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    form = models.CharField(
        max_length=32,
        blank=True,
        null=True
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

    @transaction.atomic
    def activate_tag(self, user):
        self.owner = user
        self.active = True
        self.save()

    @transaction.atomic
    def deactivate_tag(self):
        self.owner = None
        self.active = False
        self.save()

    def create_record(self):
        record = NearFieldCommunicationRecord.objects.create(tag=self)
        return record

    def get_mapping_url(self):
        return reverse('link-tag', args=[str(self.uuid)])

    class Meta:
        verbose_name = "near field communication tag"
        verbose_name_plural = "near field communication tags"


class NearFieldCommunicationRecord(Orderable):
    tag = ParentalKey(
        NearFieldCommunicationTag,
        on_delete=models.CASCADE,
        related_name='records'
    )
    asset = models.OneToOneField(
        'inventory.InventoryAssetPage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='linked_tag'
    )

    class Meta:
        verbose_name = _("near field communication record")
        verbose_name_plural = _("near field communication records")

