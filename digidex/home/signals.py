from django.db.models.signals import post_migrate
from django.dispatch import receiver
from wagtail.models import Site, Page

from inventory.models.landing import HomePage


@receiver(post_migrate)
def create_wagtail_site(sender, **kwargs):
    # Check if the default site already exists
    if not Site.objects.filter(is_default_site=True).exists():
        # Get the root page from Wagtail tree, which is required to attach any other page
        root_page = Page.objects.get(id=1)

        # Create the home page
        home_page = HomePage(title="Home")
        root_page.add_child(instance=home_page)
        home_page_revision = home_page.save_revision()
        home_page_revision.publish()

        site = Site(
            hostname='digidex.app',
            port=80,
            root_page=home_page,
            is_default_site=True,
            site_name='DigiDex'
        )
        site.save()
