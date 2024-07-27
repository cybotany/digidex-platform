from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from inventory.utils import user_setup
from inventory.models import UserInventory

User = get_user_model()

class Command(BaseCommand):
    help = 'Manually invoke the new_user_setup signal for all users or a specific user'

    def add_arguments(self, parser):
        parser.add_argument(
            '--user-id',
            type=int,
            help='Specify the ID of a single user to run the setup for'
        )

    def handle(self, *args, **options):
        user_id = options['user_id']
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                self.setup_user(user)
                self.stdout.write(self.style.SUCCESS(f'Successfully set up user with ID {user_id}'))
            except User.DoesNotExist:
                raise CommandError(f'User with ID {user_id} does not exist')
        else:
            users = User.objects.all()
            for user in users:
                self.setup_user(user)
            self.stdout.write(self.style.SUCCESS('Successfully set up all users'))

    def setup_user(self, user):
        created = not UserInventory.objects.filter(owner=user).exists()
        user_setup(user)
        # Manually send the signal
        post_save.send(sender=User, instance=user, created=created)
