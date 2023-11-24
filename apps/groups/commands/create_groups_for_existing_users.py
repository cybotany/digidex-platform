from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.utils.helpers import create_user_groups
from apps.utils.constants import MAX_GROUP
from apps.groups.models import Group

class Command(BaseCommand):
    help = 'Create default plant groups for existing users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            existing_groups_count = Group.objects.filter(user=user).count()
            if existing_groups_count < MAX_GROUP:
                create_user_groups(user, existing_groups_count)
                self.stdout.write(self.style.SUCCESS(f'All {MAX_GROUP} groups created or verified for user {user.username}'))
