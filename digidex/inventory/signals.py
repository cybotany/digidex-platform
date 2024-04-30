from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from inventory.models import UserIndexPage, UserPage

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_page(sender, instance, created, **kwargs):
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

@receiver(post_save, sender=User)
def create_user_collection(sender, instance, created, **kwargs):
    if created:
        # This block runs only when a new user is created
        root_collection = Collection.get_first_root_node()
        user_collection = root_collection.add_child(name=f"User {instance.username} Collection")