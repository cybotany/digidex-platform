from wagtail.models import Page, Site

from home.models import HomePage


def create_homepage():
    if HomePage.objects.exists():
        print("HomePage already exists. No action taken.")
        return

    homepage = HomePage(
        title="Home",
        slug="inventory"
    )
    root_page = Page.objects.get(id=1)
    root_page.add_child(instance=homepage)
    homepage.save_revision().publish()

    Site.objects.update_or_create(
        hostname='localhost',
        defaults={
            'port': 8000,
            'site_name': 'DigiDex (Dev)',
            'root_page': homepage,
            'is_default_site': True,
            }
    )

    print("HomePage created and set as the root page.")
    return homepage
