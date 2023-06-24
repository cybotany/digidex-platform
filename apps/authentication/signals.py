from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.authentication.models import Profile


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
