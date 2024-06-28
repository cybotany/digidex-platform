import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save

from inventory.models import InventoryPage

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Manually invoke the post-save signal for InventoryPage to create collections'

    def handle(self, *args, **options):
        try:
            inventory_pages = InventoryPage.objects.all()
            for inventory_page in inventory_pages:
                self.stdout.write(self.style.WARNING(f'Invoking signal for InventoryPage with ID {inventory_page.id}'))
                logger.debug(f'Invoking signal for InventoryPage with ID {inventory_page.id}')
                post_save.send(sender=InventoryPage, instance=inventory_page, created=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully invoked signal for InventoryPage with ID {inventory_page.id}'))
        except Exception as e:
            logger.error(f'Error invoking signals: {str(e)}')
            raise CommandError(f'Error invoking signals: {str(e)}')

        self.stdout.write(self.style.SUCCESS('Successfully invoked signals for all InventoryPages'))
