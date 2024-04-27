from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import ProfileIndexPage, ProfilePage

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile_page(sender, instance, created, **kwargs):
    if created:
        root_profile_page = ProfileIndexPage.objects.first()
        if root_profile_page:
            user_profile_page = ProfilePage(
                title=f"{instance.username}'s Profile",
                user=instance,
                slug=instance.slug
            )
            root_profile_page.add_child(instance=user_profile_page)
            user_profile_page.save_revision().publish()
