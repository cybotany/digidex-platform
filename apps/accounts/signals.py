from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.accounts.models import Profile
from apps.botany.models import Group
from apps.utils.constants import MAX_GROUP

@receiver(post_save, sender=get_user_model())
def manage_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a user profile whenever a user instance is created or saved.

    Args:
        sender: The model class sending the signal.
        instance: The actual instance of the sender model.
        created: Boolean; True if a new record was created.
    """
    Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=get_user_model())
def manage_user_group(sender, instance, created, **kwargs):
    """
    Signal handler to create default groups for the user 
    whenever a new user instance is created.

    Args:
        sender: The model class sending the signal.
        instance: The actual instance of the sender model.
        created: Boolean; True if a new record was created.
    """
    if created:
        for i in range(1, MAX_GROUP+1):
            Group.objects.create(
                name=f'Group {i}',
                user=instance
            )
