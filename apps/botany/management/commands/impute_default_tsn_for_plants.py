from django.core.management.base import BaseCommand
from apps.botany.models import Plant
from apps.itis.models import TaxonomicUnits


class Command(BaseCommand):
    help = 'Update plants with null TSN to have a default Taxonomic Unit'

    def handle(self, *args, **kwargs):
        default_taxonomic_unit = TaxonomicUnits.objects.get(tsn=202422)
        plants_to_update = Plant.objects.filter(tsn__isnull=True)
        count = plants_to_update.count()

        plants_to_update.update(tsn=default_taxonomic_unit)

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {count} plants with default TSN.'))
