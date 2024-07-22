from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from inventory.utils import create_user_inventory, create_user_party


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_inventory(sender, instance, created, **kwargs):
    if created:        
        user_inventory = create_user_inventory(instance)
        user_party = create_user_party(user_inventory)
