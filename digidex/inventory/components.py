from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component


class HeadingPanel(Component):
    template_name = 'inventory/panels/heading.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['heading'] = parent_context['request'].user.username
        context['paragraph'] = 'Welcome to the inventory app!'
        return context

    class Media:
        css = {
            'all': ('inventory/css/heading.css',)
        }


class CategoryPanel(Component):
    template_name = 'inventory/panels/category.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/category.css',)
        }


class ItemPanel(Component):
    template_name = 'inventory/panels/item.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/item.css',)
        }
