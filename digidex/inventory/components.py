from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
)
from home.components import (
    NavigationComponent,
    HeaderComponent,
)


class InventoryDashboardComponent(Component):
    template_name = 'inventory/components/inventory_dashboard.html'

    def __init__(self, request):
        self.user = request.user
        self.is_authenticated = request.user.is_authenticated

    def get_inventory(self):
        from inventory.models import InventoryPage
        return InventoryPage.objects.get(owner=self.user)

    def get_categories(self):
        inventory = self.get_inventory()
        return inventory.get_categories()

    def get_heading(self):
        inventory = self.get_inventory()
        return inventory.title

    def get_navigation_panel(self):
        return NavigationComponent(self.user)

    def get_header_panel(self):
        from category.components import CategoryCollectionComponent
        categories = CategoryCollectionComponent(list(self.get_categories()))
        heading = self.get_heading()
        return HeaderComponent(
            {
                "heading": heading,
                "categories": categories,
            }
        )

    def get_login_panel(self):
        pass

    def get_header_panels(self):
        panels = [
            self.get_navigation_panel(),
        ]
        if self.is_authenticated:
            panels.append(self.get_header_panel())
        return panels

    def get_body_panels(self):
        panels = []
        if self.is_authenticated:
            pass
        else:
            panels.append(self.get_login_panel())
        return panels

    def get_footer_panels(self):
        panels = []
        if self.is_authenticated:
            pass
        else:
            pass
        return panels

    def get_context_data(self, parent_context=None):
        header = self.get_header_panels()
        body = self.get_body_panels()
        footer = self.get_footer_panels()
        return {
            "header_panels": header if header else None,
            "body_panels": body if body else None,
            "footer_panels": footer if footer else None,
        }
