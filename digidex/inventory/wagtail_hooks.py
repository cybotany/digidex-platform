from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.admin.ui.components import Component
from wagtail.admin.site_summary import SummaryItem
from wagtail import hooks


class WelcomePanel(Component):
    order = 50

    def render_html(self, parent_context):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>Welcome to the DigiDex Inventory System</h3>
        </section>
        """)

@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())

@hooks.register("construct_homepage_summary_items", order=1)
def hide_images_and_documents_from_partners(request, summary_items):
    summary_items.clear()

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('base/css/digidex.css'))
