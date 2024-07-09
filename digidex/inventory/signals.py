from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from wagtail.models import Collection, Page

from inventory.models import InventoryIndex, InventoryCategory

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_inventory(sender, instance, created, **kwargs):
    if created:
        name = instance.username.title()
        
        parent_collection = Collection.get_first_root_node()
        user_collection = parent_collection.add(name=name)

        root_page = Page.objects.get(depth=1)
        inventory = InventoryIndex(
            title=f"{name}'s Inventory",
            name=name,
            slug=slugify(name),
            owner=instance,
            collection=user_collection
        )
        root_page.add_child(instance=inventory)

@receiver(post_save, sender=InventoryIndex)
def create_user_menu_category(sender, instance, created, **kwargs):
    if created:
        name = "Menu"

        parent_collection = instance.collection
        category_collection = parent_collection.add(name=name)

        category = InventoryCategory(
            title=name,
            name=name,
            slug=slugify(name),
            owner=instance.owner,
            collection=category_collection
        )
        instance.add_child(instance=category)
