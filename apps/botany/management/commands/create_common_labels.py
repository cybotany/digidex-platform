from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from apps.botany.models import Label


class Command(BaseCommand):
    help = 'Create common labels for existing users'

    def handle(self, *args, **options):
        common_labels = ['Label 1', 'Label 2', 'Label 3']  # Replace these with your common labels
        
        # Fetch all users
        users = get_user_model().objects.all()

        # Loop through all users
        for user in users:
            # For each user, create the common labels
            for label in common_labels:
                Label.objects.get_or_create(user=user, name=label, is_common=True)

        # Output completion message
        self.stdout.write(self.style.SUCCESS('Successfully created common labels for existing users'))
