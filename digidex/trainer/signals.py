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
