from wagtail import hooks

from inventory.components import InventorySummaryItem, WelcomePanel

    
@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())

@hooks.register("construct_homepage_summary_items", order=1)
def show_inventory_summary(request, summary_items):
    summary_items.append(InventorySummaryItem(request))

# @hooks.register('insert_global_admin_css')
# def global_admin_css():
#     return format_html('<link rel="stylesheet" href="{}">', static('base/css/digidex.css'))
