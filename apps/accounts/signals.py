from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.accounts.models import Profile

@receiver(post_save, sender=get_user_model())
def manage_user_creation(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a user profile whenever a user instance is created or saved.
    """
    Profile.objects.get_or_create(user=instance)
