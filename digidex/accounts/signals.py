import logging
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from wagtail.models import Site

from accounts.models import User, UserProfile, UserProfileIndexPage, UserProfilePage

logger = logging.getLogger(__name__)

@receiver(post_migrate)
def create_user_profile_index_page(sender, **kwargs):
    try:
        site = Site.objects.get(is_default_site=True)
        home_page = site.root_page

        if not UserProfileIndexPage.objects.descendant_of(home_page).exists():
            user_profile_index_page = UserProfileIndexPage(
                title="User Profiles",
                slug="u",
            )
            home_page.add_child(instance=user_profile_index_page)
            user_profile_index_page.save_revision().publish()
    except ObjectDoesNotExist:
        logger.error("Default site or home page does not exist.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

@receiver(post_save, sender=User)
def ensure_user_collection_exists(sender, instance, created, **kwargs):
    if created:
        instance.create_user_collection()

@receiver(post_save, sender=UserProfile)
def create_user_profile_page(sender, instance, created, **kwargs):
    if created:
        instance.create_user_profile_page()

@receiver(post_save, sender=UserProfilePage)
def create_user_inventory(sender, instance, created, **kwargs):
    if created:
        try:
            instance.create_inventory_page()
        except IntegrityError as e:
            logger.error(f"Database integrity error: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred when creating user inventory: {e}")
