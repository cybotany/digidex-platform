# myapp/management/commands/create_party_category.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify

from inventory.models import UserProfileIndexPage, UserProfilePage
from inventory.signals import create_default_category

class Command(BaseCommand):
    help = 'Manually create a party category for an existing user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user to create the party category for')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
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
                user_profile_index = UserProfileIndexPage.objects.first()
                if user_profile_index:
                    user_profile_index.add_child(instance=user_profile_page)
                    user_profile_page.save_revision().publish()
                    self.stdout.write(self.style.SUCCESS(f'Successfully created UserProfilePage for user {username}'))

            # Now create the party category
            create_default_category(sender=UserProfilePage, instance=user_profile_page, created=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully ensured party category for user {username}'))
        
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with username {username} does not exist'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
