from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.groups.models import Group
from apps.utils.constants import MAX_GROUP


class Command(BaseCommand):
    help = 'Create default plant groups for existing users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            # Check if the user already has the max amount of groups
            existing_groups_count = Group.objects.filter(user=user).count()

            if existing_groups_count < MAX_GROUP:
                for i in range(existing_groups_count + 1, MAX_GROUP+1):
                    Group.objects.create(user=user, name=f'Group {i}', position=i)
                    self.stdout.write(self.style.SUCCESS(f'Created Group {i} for user {user.username}'))

                self.stdout.write(self.style.SUCCESS(f'All {MAX_GROUP} groups created for user {user.username}'))