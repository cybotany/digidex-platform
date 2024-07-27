from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from inventory.utils import create_user_inventory


User = get_user_model()

@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    if created:        
        user_inventory = create_user_inventory(instance)
