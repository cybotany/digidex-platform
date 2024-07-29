from wagtail.models import Page, Site, Collection

from home.models import HomePage


def create_homepage():
    if HomePage.objects.exists():
        print("HomePage already exists. No action taken.")
        return

    root_collection = Collection.get_first_root_node()
    home_collection = root_collection.add_child(name="Home")

    homepage = HomePage(
        title="Home",
        slug="inventory",
        collection=home_collection,
    )
    root_page = Page.objects.get(id=1)
    root_page.add_child(instance=homepage)
    homepage.save_revision().publish()

    Site.objects.update_or_create(
        hostname='digidex.tech',
        defaults={
            'port': 80,
            'site_name': 'DigiDex',
            'root_page': homepage,
            'is_default_site': True,
            }
    )

    print("HomePage created and set as the root page.")
    return homepage
