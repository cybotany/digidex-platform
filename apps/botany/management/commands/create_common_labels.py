from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from apps.botany.models import GrowingLabel
from apps.utils.constants import COMMON_LABELS


class Command(BaseCommand):
    help = 'Create common labels for existing users'

    def handle(self, *args, **options):
        # Fetch all users
        users = get_user_model().objects.all()

        # Loop through all users
        for user in users:
            # For each user, create the common labels
            for label in COMMON_LABELS:
                GrowingLabel.objects.get_or_create(user=user, name=label, is_common=True)

        # Output completion message
        self.stdout.write(self.style.SUCCESS('Successfully created common labels for existing users'))
