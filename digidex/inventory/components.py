from django.forms import Media

from laces.components import Component, MediaContainer


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

    def get_panels(self):
        panels = [
            self.get_navigation_panel(),
        ]
        if self.is_authenticated:
            panels.append(self.get_header_panel())
        return panels

    def get_context_data(self, parent_context=None):
        panels = self.get_panels()
        return {
            "panels": MediaContainer(panels),
        }
