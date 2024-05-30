from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from inventory.models import UserProfile
from inventory.utils import get_or_create_user_profile, get_or_create_user_profile_page

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a user page and user profile for any active users who don\'t currently have a profile/page.'

    def handle(self, *args, **kwargs):
        active_users_without_profile = User.objects.filter(is_active=True, profile__isnull=True)
        active_user_profiles_without_page = UserProfile.objects.filter(is_active=True, page__isnull=True)

        self.stdout.write(f'Found {active_users_without_profile.count()} active users without a profile.')
        self.stdout.write(f'Found {active_user_profiles_without_page.count()} active users without a page.')

        for user in active_users_without_profile:
            get_or_create_user_profile(user)
            self.stdout.write(self.style.SUCCESS(f'Created profile for user {user.username}'))

        for user in active_user_profiles_without_page:
            get_or_create_user_profile_page(user.profile)
            self.stdout.write(self.style.SUCCESS(f'Created page for user {user.username}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated user data.'))
