from django.utils.text import slugify

from wagtail.models import Collection, Page

from inventory.models import UserInventoryIndex


def get_root_inventory_collection():
    root_collection = Collection.get_first_root_node()
    inventory_collection, _ = root_collection.get_children().get_or_create(name="Inventory")
    return inventory_collection

def get_homepage():
    homepage = Page.objects.filter(slug='home', depth=2).first()
    if not homepage:
        from home.utils import create_homepage
        homepage = create_homepage()
    return homepage

def create_user_inventory(user):
    username = user.username.title()

    root_inventory_collection = get_root_inventory_collection()
    user_inventory_collection, _ = root_inventory_collection.get_children().get_or_create(name=username)

    user_inventory = UserInventoryIndex(
        title=f"{username}'s Inventory",
        slug=slugify(username),
        owner=user,
        collection=user_inventory_collection
    )
    homepage = get_homepage()
    homepage.add_child(instance=user_inventory)
    user_inventory.save_revision().publish()
    return user_inventory

def create_user_party(user_inventory):
    user_party = user_inventory.create_category("Party")
    return user_party
