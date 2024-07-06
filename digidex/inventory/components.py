from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component
from wagtail.admin.site_summary import SummaryItem


class WelcomePanel(Component):
    order = 50

    def render_html(self, parent_context):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>Welcome to the DigiDex Inventory System</h3>
        </section>
        """)
    
    class Media:
        css = {
            'all': ['base/css/digidex.css']
        }


class InventorySummaryItem(SummaryItem):
    template_name = 'inventory/summary_panel.html'

    def get_context(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ['base/css/digidex.css']
        }
