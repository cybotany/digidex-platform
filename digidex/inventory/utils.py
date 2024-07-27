from django.utils.text import slugify

from wagtail.models import Collection

from inventory.models import UserInventory


def _create_user_inventory_collection(user_inventory):
    root = Collection.get_first_root_node()
    root_children = root.get_children()
    try:
        inventory = root_children.get(name='Inventory')
    except Collection.DoesNotExist:
        inventory = root.add_child(name="Inventory")

    # Using the UUID as the collection name to ensure uniqueness and avoid conflicts
    inventory_uuid = str(user_inventory.uuid)
    inventory_children = inventory.get_children()
    try:
        collection = inventory_children.get(name=inventory_uuid)
    except Collection.DoesNotExist:
        collection = inventory.add_child(name=inventory_uuid)
    return collection

def _create_user_inventory(user):
    username = user.username
    inventory = UserInventory.objects.create(
        owner=user,
        slug=slugify(username),
        name=f"{username.title()}'s Inventory"
    )
    return inventory

def user_setup(user):
    inventory = _create_user_inventory(user)
    collection = _create_user_inventory_collection(inventory)
    inventory.collection = collection
    inventory.save()
    return inventory
