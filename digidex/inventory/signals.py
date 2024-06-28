import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from .models import InventoryPage

logger = logging.getLogger(__name__)

def get_or_create_inventory_collection(trainer_collection, inventory_name):
    # Search only within the children of the trainer collection
    try:
        inventory_collection = trainer_collection.get_children().get(name=inventory_name)
        logger.debug(f"Inventory collection found: {inventory_collection}")
    except Collection.DoesNotExist:
        inventory_collection = trainer_collection.add_child(name=inventory_name)
        logger.debug(f"Created inventory collection: {inventory_collection}")
    return inventory_collection

@receiver(post_save, sender=InventoryPage)
def create_new_inventory_collection(sender, instance, created, **kwargs):
    if created:
        logger.debug(f"Creating new inventory collection for instance: {instance}")
        trainer_page = instance.get_parent().specific
        trainer_collection = trainer_page.collection
        inventory_collection = get_or_create_inventory_collection(trainer_collection, instance.title)
        instance.collection = inventory_collection
        instance.save()
        logger.debug(f"Inventory collection set for instance: {instance}")
