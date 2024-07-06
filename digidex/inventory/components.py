from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component


class WelcomePanel(Component):
    order = 50
    template_name = 'inventory/panels/welcome.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/inventory.css',)
        }



class CatagoryPanel(Component):
    template_name = 'inventory/panels/catagory.html'

    class Media:
        css = {
            'all': ('inventory/css/inventory.css',)
        }
