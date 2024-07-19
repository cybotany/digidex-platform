from laces.components import Component


class InventoryDashboard(Component):
    template_name = 'inventory/panels/inventory_dashboard.html'

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
        pass

    def get_context_data(self, parent_context=None):
        pass
