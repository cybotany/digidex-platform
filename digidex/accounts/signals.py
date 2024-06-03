from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from inventory.models import UserProfilePage, UserProfileIndexPage


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile_index = UserProfileIndexPage.objects.first()
        UserProfilePage.objects.create(
            title=f"{instance.username}'s Profile",
            slug=instance.username,
            owner=instance,
            heading=f"{instance.username}'s Profile",
            introduction="Welcome to my profile!",
            live=True,
            path=user_profile_index.path + instance.username + '/',
            depth=user_profile_index.depth + 1,
            numchild=0
        )
