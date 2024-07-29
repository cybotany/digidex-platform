from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from home.models import HomePage
from inventory.models import UserInventoryIndex


User = get_user_model()

@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    if created:
        home_page = HomePage.objects.first()
        user_inventory_page = UserInventoryIndex(
            title=f"{instance.username.title()}'s Inventory",
            slug=slugify(instance.username),
            owner=instance
        )
        home_page.add_child(instance=user_inventory_page)
        user_inventory_page.save_revision().publish()
