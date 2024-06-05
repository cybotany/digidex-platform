import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from wagtail.models import Collection

from inventory.models import UserProfileIndexPage, UserProfilePage, InventoryCategoryPage

logger = logging.getLogger(__name__)

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            slug = slugify(instance.username)
            user_profile_index = UserProfileIndexPage.objects.first()
            if user_profile_index:
                user_profile_page = UserProfilePage(
                    title=f"{instance.username}'s Profile",
                    slug=slug,
                    owner=instance,
                    heading=f"{instance.username}'s Profile",
                    introduction="Welcome to my profile!"
                )
                user_profile_index.add_child(instance=user_profile_page)
                user_profile_page.save_revision().publish()

                root_users_collection, created = Collection.objects.get_or_create(name='Users')
                user_collection = Collection.objects.create(name=f"{instance.username}'s Collection", parent=root_users_collection)
                user_collection.save()            
            else:
                logger.error("UserProfileIndexPage does not exist.")
        except Exception as e:
            logger.error(f"Error creating UserProfilePage: {e}")

@receiver(post_save, sender=UserProfilePage)
def create_default_category(sender, instance, created, **kwargs):
    if created:
        try:
            inventory_category_page = InventoryCategoryPage(
                title=f"{instance.owner.username}'s Inventory - Party",
                slug='party',
                owner=instance.owner,
                name="Party",
                description=f"{instance.owner.username}'s Party",
                is_party=True
            )
            instance.add_child(instance=inventory_category_page)
            inventory_category_page.save_revision().publish()
        except Exception as e:
            logger.error(f"Error creating InventoryCategoryPage: {e}")
