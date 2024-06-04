from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from inventory.models import UserProfileIndexPage, UserProfilePage
from inventory.signals import create_default_category

User = get_user_model()

class Command(BaseCommand):
    help = 'Manually create a party category for all existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        user_profile_index = UserProfileIndexPage.objects.first()

        if not user_profile_index:
            self.stdout.write(self.style.ERROR('UserProfileIndexPage does not exist.'))
            return

        for user in users:
            try:
                user_profile_page, created = UserProfilePage.objects.get_or_create(
                    owner=user,
                    defaults={
                        'title': f"{user.username}'s Profile",
                        'slug': slugify(user.username),
                        'heading': f"{user.username}'s Profile",
                        'introduction': "Welcome to my profile!"
                    }
                )
                
                if created:
                    # Adding the newly created UserProfilePage to UserProfileIndexPage
                    user_profile_index.add_child(instance=user_profile_page)
                    user_profile_page.save_revision().publish()
                    self.stdout.write(self.style.SUCCESS(f'Successfully created UserProfilePage for user {user.username}'))

                # Now create the party category
                create_default_category(sender=UserProfilePage, instance=user_profile_page, created=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully ensured party category for user {user.username}'))
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing user {user.username}: {e}'))

        self.stdout.write(self.style.SUCCESS('Process completed for all users.'))
