from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from profiles.utils import create_user_profile

User = get_user_model()

@receiver(post_save, sender=User)
def user_profile_signal(sender, instance, created, **kwargs):
    """
    Signal to create a user profile immediately a new user instance is created.
    """
    pass
    #if created:
    #    create_user_profile(instance)
