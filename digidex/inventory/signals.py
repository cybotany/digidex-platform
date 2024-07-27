from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from inventory.models import UserInventory


User = get_user_model()

@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    if created:        
        UserInventory.objects.create(
            name=f"{instance.username.title()}'s Inventory",
            slug=slugify(instance.username),
            owner=instance
        )
