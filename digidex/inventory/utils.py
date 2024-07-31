from wagtail.models import Page, Site, Collection

from inventory.models import InventoryIndexPage


def create_inventory_index():
    if InventoryIndexPage.objects.exists():
        print("HomePage already exists. No action taken.")
        return

    root_collection = Collection.get_first_root_node()
    home_collection = root_collection.add_child(name="Home")

    inventory_index = InventoryIndexPage(
        title="Home",
        slug="inventory",
        collection=home_collection,
    )
    root_page = Page.objects.get(id=1)
    root_page.add_child(instance=inventory_index)
    inventory_index.save_revision().publish()

    print("InventoryIndexPage created.")
    return inventory_index
