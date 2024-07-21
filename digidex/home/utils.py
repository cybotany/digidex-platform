from wagtail.models import Page, Site

from home.models import HomePage


def create_homepage():
    if HomePage.objects.exists():
        print("HomePage already exists. No action taken.")
        return

    root_page = Page.objects.get(id=1)  # Get the root page
    homepage = HomePage(
        title="Home",
        slug="home",
    )
    root_page.add_child(instance=homepage)
    homepage.save_revision().publish()

    # Set the site root page
    Site.objects.update_or_create(
        hostname='',
        is_default_site=True,
        defaults={'root_page': homepage}
    )
    print("HomePage created and set as the root page.")
