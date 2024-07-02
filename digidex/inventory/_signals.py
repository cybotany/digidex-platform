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


import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from .models import AssetPage

logger = logging.getLogger(__name__)

def get_or_create_asset_collection(inventory_collection, asset_name):
    # Search only within the children of the inventory collection
    try:
        asset_collection = inventory_collection.get_children().get(name=asset_name)
        logger.debug(f"Asset collection found: {asset_collection}")
    except Collection.DoesNotExist:
        asset_collection = inventory_collection.add_child(name=asset_name)
        logger.debug(f"Created asset collection: {asset_collection}")
    return asset_collection

@receiver(post_save, sender=AssetPage)
def create_new_asset_collection(sender, instance, created, **kwargs):
    if created:
        logger.debug(f"Creating new asset collection for instance: {instance}")
        inventory_page = instance.get_parent().specific
        inventory_collection = inventory_page.collection
        asset_collection = get_or_create_asset_collection(inventory_collection, instance.title)
        instance.collection = asset_collection
        instance.save()
        logger.debug(f"Asset collection set for instance: {instance}")


import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from .models import TrainerPage

logger = logging.getLogger(__name__)

def get_or_create_root_collection():
    root_collection = Collection.get_first_root_node()
    logger.debug(f"Root collection found: {root_collection}")
    if not root_collection:
        logger.debug("Root collection not found, creating a new one.")
        root_collection = Collection.add_root(name='Root')
        if not root_collection:
            logger.error("Failed to create root collection.")
            raise ValueError("Root collection could not be created.")
    return root_collection

def get_or_create_user_collection():
    root_collection = get_or_create_root_collection()
    try:
        user_collection = Collection.objects.get(name='Users')
        logger.debug(f"User collection found: {user_collection}")
    except Collection.DoesNotExist:
        logger.debug("User collection not found, creating a new one.")
        user_collection = root_collection.add_child(name='Users')
        if not user_collection:
            logger.error("Failed to create user collection.")
            raise ValueError("User collection could not be created or found.")
    return user_collection

def get_or_create_trainer_collection(user):
    user_collection = get_or_create_user_collection()
    try:
        trainer_collection = Collection.objects.get(name=user.username)
        logger.debug(f"Trainer collection for user {user.username} found: {trainer_collection}")
    except Collection.DoesNotExist:
        logger.debug(f"Trainer collection for user {user.username} not found, creating a new one.")
        trainer_collection = user_collection.add_child(name=user.username)
        if not trainer_collection:
            logger.error(f"Failed to create trainer collection for user {user.username}.")
            raise ValueError(f"Trainer collection for user {user.username} could not be created or found.")
    return trainer_collection

@receiver(post_save, sender=TrainerPage)
def create_new_trainer_collection(sender, instance, created, **kwargs):
    if created:
        logger.debug(f"Creating new trainer collection for instance: {instance}")
        trainer_collection = get_or_create_trainer_collection(instance.owner)
        instance.collection = trainer_collection
        instance.save()
        logger.debug(f"Trainer collection set for instance: {instance}")
