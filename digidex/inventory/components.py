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


class InventoryDashboardComponent(Component):
    template_name = 'inventory/components/dashboard.html'

    def __init__(self, user):
        self.user = user
        self.is_authenticated = user.is_authenticated

    def get_inventory(self):
        from inventory.models import InventoryPage
        return InventoryPage.objects.get(owner=self.user)
