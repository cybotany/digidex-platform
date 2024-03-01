from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from digidex.inventory.models import profile as app_profile
from digidex.inventory.models import grouping as digit_group

@receiver(post_save, sender=get_user_model())
def manage_user_creation(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a user profile whenever a user instance is created or saved.
    """
    profile, _ = app_profile.Profile.objects.get_or_create(user=instance)

    if created:
        digit_group.Grouping.objects.create(
            user=instance,
            name="Default Group",
            description="Automatically created default group.",
            is_default=True
        )
