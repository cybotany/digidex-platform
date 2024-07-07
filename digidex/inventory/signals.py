from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from inventory.models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.profile:
            user_profile = UserProfile.objects.get_or_create(
                user=instance,
                inventory=None
            )
        user_inv = user_profile.setup_inventory()
