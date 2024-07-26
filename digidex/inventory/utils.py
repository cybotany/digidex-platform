from django.utils.text import slugify

from wagtail.models import Collection

from inventory.models import UserInventory


def get_root_inventory_collection():
    root_collection = Collection.get_first_root_node()
    inventory_collection, _ = root_collection.get_children().get_or_create(name="Inventory")
    return inventory_collection

def create_user_inventory(user):
    username = user.username.title()

    root_inventory_collection = get_root_inventory_collection()
    user_inventory_collection, _ = root_inventory_collection.get_children().get_or_create(name=username)

    user_inventory = UserInventory.objects.create(
        owner=user,
        slug=slugify(username),
        collection=user_inventory_collection
    )
    return user_inventory
