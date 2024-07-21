from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from wagtail.models import Collection, Page

from inventory.models import InventoryPage


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_inventory(sender, instance, created, **kwargs):
    if created:
        name = instance.username.title()
        
        parent_collection = Collection.get_first_root_node()
        user_collection = parent_collection.add_child(name=name)

        # Create user's inventory
        root_page = Page.objects.get(depth=1)
        user_inventory = InventoryPage(
            title=f"{name}'s Inventory",
            slug=slugify(name),
            owner=instance,
            collection=user_collection,
            type="root"  
        )
        root_page.add_child(instance=user_inventory)

        # Create user's party
        party_collection = user_collection.add_child(name="Party")
        user_party = InventoryPage(
            title=f"{name}'s Party",
            slug="party",
            owner=instance,
            collection=party_collection,
            type="group"
        )
        user_inventory.add_child(instance=user_party)
