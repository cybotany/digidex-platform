from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from inventory.models import Grouping

User = get_user_model()

class Command(BaseCommand):
    help = 'Ensures every user has a default grouping.'

    def handle(self, *args, **options):
        users_without_default_grouping = User.objects.filter(digit_groups__is_default=True).distinct()

        for user in User.objects.exclude(id__in=users_without_default_grouping):
            default_grouping, created = Grouping.objects.get_or_create(
                user=user,
                is_default=True,
                defaults={'name': 'Default Grouping', 'description': 'Automatically created default grouping.'}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Default grouping created for {user.username}'))
            else:
                self.stdout.write(self.style.NOTICE(f'{user.username} already has a default grouping'))
