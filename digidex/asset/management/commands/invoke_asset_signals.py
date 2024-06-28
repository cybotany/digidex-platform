import logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save

from asset.models import AssetPage

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Manually invoke the post-save signal for AssetPage to create collections'

    def handle(self, *args, **options):
        try:
            asset_pages = AssetPage.objects.all()
            for asset_page in asset_pages:
                self.stdout.write(self.style.WARNING(f'Invoking signal for AssetPage with ID {asset_page.id}'))
                logger.debug(f'Invoking signal for AssetPage with ID {asset_page.id}')
                post_save.send(sender=AssetPage, instance=asset_page, created=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully invoked signal for AssetPage with ID {asset_page.id}'))
        except Exception as e:
            logger.error(f'Error invoking signals: {str(e)}')
            raise CommandError(f'Error invoking signals: {str(e)}')

        self.stdout.write(self.style.SUCCESS('Successfully invoked signals for all AssetPages'))
