from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from digidex.inventory.models import Plant, Pet
from digidex.journal.models import Collection

class Command(BaseCommand):
    help = 'Create a journal collection for every pet or plant that currently doesn\'t have one.'

    def handle(self, *args, **options):
        self.create_missing_collections_for_model(Plant)
        self.create_missing_collections_for_model(Pet)

    def create_missing_collections_for_model(self, model):
        # Get the ContentType for the current model
        content_type = ContentType.objects.get_for_model(model)

        # Find all instances of the model that do not have a Collection
        missing_collections = model.objects.annotate(
            collection_count=Count('collection')
        ).filter(collection_count=0)

        # Create a Collection for each missing instance
        for instance in missing_collections:
            Collection.objects.create(
                content_type=content_type,
                object_id=instance.id
            )
            self.stdout.write(self.style.SUCCESS(f'Created Collection for {model.__name__} with ID {instance.id}'))

        self.stdout.write(self.style.SUCCESS(f'Finished creating collections for {model.__name__}'))
