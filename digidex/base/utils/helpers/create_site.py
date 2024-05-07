from wagtail.models import Page, Site


class SiteCreator:
    @staticmethod
    def create_site(hostname, site_name, root_page_class, children_pages):
        # Create the root page under the main Wagtail root
        main_root = Page.objects.get(id=1)
        root_page = root_page_class(title=site_name + ' Root')
        main_root.add_child(instance=root_page)
        root_page.save_revision().publish()

        # Create children pages
        for child_page_class, child_title in children_pages:
            child_page = child_page_class(title=child_title)
            root_page.add_child(instance=child_page)
            child_page.save_revision().publish()

        # Create the site
        site = Site.objects.create(
            hostname=hostname,
            root_page=root_page,
            is_default_site=False,
            site_name=site_name
        )
        return site
