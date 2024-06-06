from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from wagtail.models import Collection
from django.db import transaction

from inventory.models import UserProfileIndexPage, UserProfilePage, InventoryCategoryPage

User = get_user_model()

class Command(BaseCommand):
    help = 'Manually create a user collection and party category for all existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        user_profile_index = UserProfileIndexPage.objects.first()

        if not user_profile_index:
            self.stdout.write(self.style.ERROR('UserProfileIndexPage does not exist.'))
            return

        for user in users:
            try:
                with transaction.atomic():
                    self.create_user_profile_and_collections(user, user_profile_index)
                    self.stdout.write(self.style.SUCCESS(f'Successfully processed assets for user {user.username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing user {user.username}: {e}'))

        self.stdout.write(self.style.SUCCESS('Process completed for all users.'))

    def create_user_profile_and_collections(self, user, user_profile_index):
        # Create or get the UserProfilePage
        user_profile_page = self.create_user_profile_page(user, user_profile_index)

        # Create root collection for users if it does not exist
        root_collection = Collection.get_first_root_node()
        root_users_collection = self.get_or_create_root_users_collection(root_collection)

        # Create user collection if it does not exist
        user_collection = self.create_user_collection(user, root_users_collection)

        # Create inventory category page
        self.create_inventory_category_page(user, user_profile_page)

    def create_user_profile_page(self, user, user_profile_index):
        if not UserProfilePage.objects.filter(slug=slugify(user.username)).exists():
            user_profile_page = UserProfilePage(
                title=f"{user.username}'s Profile",
                slug=slugify(user.username),
                owner=user,
                heading=f"{user.username}'s Profile",
                introduction="Welcome to my profile!",
                user=user
            )
            user_profile_index.add_child(instance=user_profile_page)
            user_profile_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f'Successfully created UserProfilePage for user {user.username}'))
        else:
            user_profile_page = UserProfilePage.objects.get(slug=slugify(user.username))
        return user_profile_page

    def get_or_create_root_users_collection(self, root_collection):
        try:
            root_users_collection = Collection.objects.get(name='Users')
        except Collection.DoesNotExist:
            root_users_collection = Collection(name='Users')
            root_collection.add_child(instance=root_users_collection)
            self.stdout.write(self.style.SUCCESS(f'Successfully created root collection for users'))
        return root_users_collection

    def create_user_collection(self, user, root_users_collection):
        user_collection = Collection(
            name=f"{user.username}'s Collection",
        )
        root_users_collection.add_child(instance=user_collection)
        self.stdout.write(self.style.SUCCESS(f'Successfully created collection for user {user.username}'))
        return user_collection

    def create_inventory_category_page(self, user, user_profile_page):
        if not InventoryCategoryPage.objects.filter(slug='party', owner=user).exists():
            inventory_category_page = InventoryCategoryPage(
                title=f"{user.username}'s Inventory - Party",
                slug='party',
                owner=user,
                name="Party",
                description=f"{user.username}'s Party",
                is_party=True
            )
            user_profile_page.add_child(instance=inventory_category_page)
            inventory_category_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS(f'Successfully created party category for user {user.username}'))
