import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save

from inventory.models import Inventory

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Manually invoke the post-save signal for Inventory to create collections'

    def handle(self, *args, **options):
        try:
            inventories = Inventory.objects.all()
            for inventory in inventories:
                self.stdout.write(self.style.WARNING(f'Invoking signal for Inventory with ID {inventory.id}'))
                logger.debug(f'Invoking signal for Inventory with ID {inventory.id}')
                post_save.send(sender=Inventory, instance=inventory, created=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully invoked signal for Inventory with ID {inventory.id}'))
        except Exception as e:
            logger.error(f'Error invoking signals: {str(e)}')
            raise CommandError(f'Error invoking signals: {str(e)}')

        self.stdout.write(self.style.SUCCESS('Successfully invoked signals for all Inventorys'))
