from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from wagtail.models import Collection, Page

from inventory.models import UserInventoryIndex, UserInventory


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_inventory(sender, instance, created, **kwargs):
    if created:        
        root_collection = Collection.get_first_root_node()
        inventory_collection, _ = root_collection.get_children().get_or_create(name="Inventory")

        username = instance.username.title()
        user_collection, _ = inventory_collection.get_children().get_or_create(name=username)

        homepage = Page.objects.filter(slug='home', depth=2).first()
        if not homepage:
            from home.utils import create_homepage
            homepage = create_homepage()

        # Create user's inventory
        user_inventory_index = UserInventoryIndex(
            title=f"{username}'s Inventory",
            slug=slugify(username),
            owner=instance,
            collection=user_collection
        )
        homepage.add_child(instance=user_inventory_index)
        user_inventory_index.save_revision().publish()

        # Create user's party
        user_party_collection = user_collection.add_child(name="Party")
        user_party_inventory = UserInventory(
            title=f"{username}'s Party",
            slug="party",
            owner=instance,
            collection=user_party_collection,
            type="folder"
        )
        user_inventory_index.add_child(instance=user_party_inventory)
        user_party_inventory.save_revision().publish()
