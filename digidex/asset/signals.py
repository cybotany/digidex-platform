import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from .models import AssetPage

logger = logging.getLogger(__name__)

def get_or_create_asset_collection(trainer_collection, asset_name):
    # Search only within the children of the trainer collection
    try:
        asset_collection = trainer_collection.get_children().get(name=asset_name)
        logger.debug(f"Asset collection found: {asset_collection}")
    except Collection.DoesNotExist:
        asset_collection = trainer_collection.add_child(name=asset_name)
        logger.debug(f"Created asset collection: {asset_collection}")
    return asset_collection

@receiver(post_save, sender=AssetPage)
def create_new_asset_collection(sender, instance, created, **kwargs):
    if created:
        logger.debug(f"Creating new asset collection for instance: {instance}")
        trainer_page = instance.get_parent().specific
        trainer_collection = trainer_page.collection
        asset_collection = get_or_create_asset_collection(trainer_collection, instance.title)
        instance.collection = asset_collection
        instance.save()
        logger.debug(f"Asset collection set for instance: {instance}")
