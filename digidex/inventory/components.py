from django.forms import Media

from laces.components import Component


class Section(Component):
    template_name = "inventory/components/section.html"

    def __init__(self, children: list[Component]):
        self.children = children

    def get_context_data(self, parent_context=None):
        return {"children": self.children}

class Heading(Component):
    template_name = 'inventory/components/heading.html'

    @property
    def media(self):
        return Media(
            css = {'all': ('inventory/css/heading.css',)}
        )


class Category(Component):
    template_name = 'inventory/components/category.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/category.css',)
        }


class Item(Component):
    template_name = 'inventory/components/item.html'

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/item.css',)
        }


class Dashboard(Component):
    template_name = "inventory/components/dashboard.html"

    def __init__(self, user):
        self.heading = Heading(
            heading=user.username.title(),
            paragraph="Welcome to your inventory dashboard!"
        )
        ...

    def get_context_data(self, parent_context=None):
        return {"heading": self.heading}
