from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component


class WelcomePanel(Component):
    order = 50
    template_name = 'inventory/welcome_panel.html'

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
