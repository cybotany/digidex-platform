from laces.components import Component

class Category(Component):
    template_name = 'inventory/components/category.html'

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['username'] = parent_context['request'].user.username
        return context

    class Media:
        css = {
            'all': ('inventory/css/category.css',)
        }
