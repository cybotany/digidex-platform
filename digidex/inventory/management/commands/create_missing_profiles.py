from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from digidex.inventory.models import Profile

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates profiles for users who do not have one.'

    def handle(self, *args, **options):
        for user in User.objects.all():
            Profile.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Ensured profile exists for user {user.username}'))
