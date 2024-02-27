from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from digidex.link.models import NTAG

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates profiles for users who do not have one.'

    def handle(self, *args, **options):
        ntags_to_update = NTAG.objects.filter(type='', use='')
        updated_count = 0
        for ntag in ntags_to_update:
            ntag.type = NTAG._meta.get_field('type').get_default()
            ntag.use = NTAG._meta.get_field('use').get_default()
            ntag.save()
            updated_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} NTAGs with default type and use.'))
