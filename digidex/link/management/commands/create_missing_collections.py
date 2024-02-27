from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from digidex.inventory.models import Plant, Pet
from digidex.journal.models import Collection

class Command(BaseCommand):
    help = 'Create a journal collection for every pet or plant that currently doesn\'t have one.'

    def handle(self, *args, **options):
        for model in [Plant, Pet]:
            self.create_missing_collections_for_model(model)

    def create_missing_collections_for_model(self, model):
        content_type = ContentType.objects.get_for_model(model)
        model_ids_with_collections = Collection.objects.filter(
            content_type=content_type
        ).values_list('object_id', flat=True)

        missing_collections = model.objects.exclude(
            id__in=model_ids_with_collections
        )

        for instance in missing_collections:
            Collection.objects.create(
                content_type=content_type,
                object_id=instance.id
            )
            self.stdout.write(self.style.SUCCESS(f'Created Collection for {model.__name__} with ID {instance.id}'))

        self.stdout.write(self.style.SUCCESS(f'Finished creating collections for {model.__name__}'))
