from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from inventory.models import UserIndexPage, UserPage

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile_page(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            root_user_page = UserIndexPage.objects.first()
            if root_user_page:
                user_page = UserPage(
                    title=f"{instance.username}'s Inventory",
                    user=instance,
                    slug=instance.slug
                )
                root_user_page.add_child(instance=user_page)
                user_page.save_revision().publish()
