from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from wagtail.models import Site

from accounts.models import UserProfile, UserProfileIndexPage, UserProfilePage

@receiver(post_migrate)
def create_user_profile_index_page(sender, **kwargs):
    """
    Creates a UserProfileIndexPage under the home page of the default site upon migration.
    This function is idempotent and will not create a new index page if one already exists.
    """
    site = Site.objects.get(is_default_site=True)
    home_page = site.root_page

    if not UserProfileIndexPage.objects.descendant_of(home_page).exists():
        user_profile_index_page = UserProfileIndexPage(
            title="User Profiles",
            slug="u",
        )
        home_page.add_child(instance=user_profile_index_page)
        user_profile_index_page.save_revision().publish()

@receiver(post_save, sender=UserProfile)
def create_user_profile_page(sender, instance, created, **kwargs):
    if created:
        user_profile_index_page = UserProfileIndexPage.objects.get(title='User Profiles')
        user_page = instance.create_user_profile_page(user_profile_index_page)
        user_collection = user_page.create_user_collection()
        user_page.set_collection_permissions(user_collection)

@receiver(post_save, sender=UserProfilePage)
def create_user_inventory_page(sender, instance, created, **kwargs):
    if created:
        instance.create_user_inventory_page()
