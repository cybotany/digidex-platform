from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save

from trainer.models import TrainerPage

class Command(BaseCommand):
    help = 'Manually invoke the post-save signal for TrainerPage to create collections'

    def handle(self, *args, **options):
        try:
            trainer_pages = TrainerPage.objects.all()
            for trainer_page in trainer_pages:
                post_save.send(sender=TrainerPage, instance=trainer_page, created=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully invoked signal for TrainerPage with ID {trainer_page.id}'))
        except Exception as e:
            raise CommandError(f'Error invoking signals: {str(e)}')

        self.stdout.write(self.style.SUCCESS('Successfully invoked signals for all TrainerPages'))
