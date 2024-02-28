# myapp/management/commands/populate_ntag_slugs.py
from django.core.management.base import BaseCommand
from digidex.link.models import NTAG
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populates slug field for NTAG instances using their serial_number'

    def handle(self, *args, **kwargs):
        ntag_instances = NTAG.objects.filter(slug__exact='')
        updated_count = 0

        for instance in ntag_instances:
            instance.slug = slugify(instance.serial_number.replace(':', '-'))
            instance.save()
            updated_count += 1
            self.stdout.write(self.style.SUCCESS(f'Updated slug for {instance.serial_number}'))

        self.stdout.write(self.style.SUCCESS(f'Finished updating slugs for {updated_count} NTAG instances.'))
