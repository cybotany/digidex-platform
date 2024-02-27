from django.core.management.base import BaseCommand
from django.utils.text import slugify
from digidex.inventory.models import Grouping

class Command(BaseCommand):
    help = 'Generates and assigns slugs for any Grouping objects that do not currently have one.'

    def handle(self, *args, **kwargs):
        groupings_without_slugs = Grouping.objects.filter(slug='')

        for grouping in groupings_without_slugs:
            # Generate a slug from the name
            slug = slugify(grouping.name)
            # Ensure the slug is unique for the user
            original_slug = slug
            num = 1
            while Grouping.objects.filter(user=grouping.user, slug=slug).exists():
                slug = f"{original_slug}-{num}"
                num += 1

            grouping.slug = slug
            grouping.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully updated slug for grouping "{grouping.name}" to "{slug}"'))
