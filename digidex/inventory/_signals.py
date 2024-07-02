from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from .models import UserProfile, InventoryCategory, MaterialEntity


def get_or_create_root_collection():
    root_collection = Collection.get_first_root_node()
    if not root_collection:
        root_collection = Collection.add_root(name='Root')
        if not root_collection:
            raise ValueError("Root collection could not be created.")
    return root_collection

def get_or_create_inventoryindex_collection():
    root_collection = get_or_create_root_collection()
    try:
        inventory_collection = Collection.objects.get(name='Inventory')
    except Collection.DoesNotExist:
        inventory_collection = root_collection.add_child(name='Inventory')
        if not inventory_collection:
            raise ValueError("User collection could not be created or found.")
    return inventory_collection

def get_or_create_userprofile_collection(user):
    inventory_collection = get_or_create_inventoryindex_collection()
    try:
        user_collection = Collection.objects.get(name=user.username)
    except Collection.DoesNotExist:
        user_collection = inventory_collection.add_child(name=user.username)
        if not user_collection:
            raise ValueError(f"User collection for user {user.username} could not be created or found.")
    return user_collection

def get_or_create_inventorycategory_collection(user_collection, category_name):
    try:
        category_collection = user_collection.get_children().get(name=category_name)
    except Collection.DoesNotExist:
        category_collection = user_collection.add_child(name=category_name)
    return category_collection

def get_or_create_materialentity_collection(category_collection, entity_name):
    try:
        entity_collection = category_collection.get_children().get(name=entity_name)
    except Collection.DoesNotExist:
        entity_collection = category_collection.add_child(name=entity_name)
    return entity_collection

@receiver(post_save, sender=UserProfile)
def create_new_userprofile_collection(sender, instance, created, **kwargs):
    if created:
        user_collection = get_or_create_userprofile_collection(instance.owner)
        instance.collection = user_collection
        instance.save()

@receiver(post_save, sender=InventoryCategory)
def create_new_inventorycategory_collection(sender, instance, created, **kwargs):
    if created:
        user = instance.get_parent().specific
        trainer_collection = trainer_page.collection
        inventory_collection = get_or_create_inventorycategory_collection(trainer_collection, instance.name)
        instance.collection = inventory_collection
        instance.save()

@receiver(post_save, sender=MaterialEntity)
def create_new_materialentity_collection(sender, instance, created, **kwargs):
    if created:
        inventory_page = instance.get_parent().specific
        inventory_collection = inventory_page.collection
        asset_collection = get_or_create_materialentity_collection(inventory_collection, instance.name)
        instance.collection = asset_collection
        instance.save()
