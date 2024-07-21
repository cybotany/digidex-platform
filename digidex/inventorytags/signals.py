from django.db.models.signals import post_save
from django.dispatch import receiver

from inventorytags.models import NearFieldCommunicationTag

@receiver(post_save, sender=NearFieldCommunicationTag)
def create_inventory_link(sender, instance, created, **kwargs):
    if created:
        instance.create_link()
