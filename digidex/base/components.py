from django.forms import Media

from laces.components import Component


class Section(Component):
    template_name = "inventory/components/section.html"

    def __init__(self, children: list[Component], style: str = None):
        self.children = children
        if style:
            self.style = f'heading-{style}'
        else:
            self.style = 'heading'

    def get_context_data(self, parent_context=None):
        return {"children": self.children}

class Heading(Component):
    template_name = 'base/components/heading.html'

    def __init__(self, text: str, size: int = 2, style: str = None):
        self.text = text
        self.size = size

        if style:
            self.style = f'heading-{style}'
        else:
            self.style = 'heading'


    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "size": self.size,
            "style": self.style
        }

    @property
    def media(self):
        return Media(
            css = {'all': ('inventory/css/heading.css',)}
        )


class Paragraph(Component):
    template_name = 'base/components/heading.html'

    def __init__(self, text: str, style: str = None):
        self.text = text
        
        if style:
            self.style = f'paragraph-{style}'
        else:
            self.style = 'paragraph'

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style}

    @property
    def media(self):
        return Media(
            css = {'all': ('inventory/css/paragraph.css',)}
        )


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
