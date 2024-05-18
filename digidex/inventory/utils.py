from django.utils.text import slugify
from wagtail.models import Page

from inventory.models import UserInventoryPage, UserInventory


def create_user_inventory_page():
    root_page = Page.objects.get(url_path='/home/')

    if not UserInventoryPage.objects.filter(slug='u').exists():
        user_inventory_page = UserInventoryPage(
            title='Inventory',
            slug='inventory',
            heading='Inventory',
            intro='Welcome to the inventory section.'
        )
        root_page.add_child(instance=user_inventory_page)
        user_inventory_page.save_revision().publish()

        print('UserInventoryPage created and added successfully!')
    else:
        print('UserInventoryPage already exists.')


def create_user_inventory(user):
    """
    Create a user inventory if it doesn't exist.
    """
    user_slug = slugify(user.username)
    inventory, created = UserInventory.objects.get_or_create(
        user=user,
        defaults={'slug': user_slug}
    )
    if created:
        inventory.save()
    return inventory
