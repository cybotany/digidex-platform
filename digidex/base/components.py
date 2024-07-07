from dataclasses import dataclass, asdict
from django.forms import Media
from laces.components import Component


class Section(Component):
    template_name = "base/components/section.html"

    def __init__(self, children: list[Component], style: str = None):
        self.children = children
        if style:
            self.style = f'section-{style}'
        else:
            self.style = 'section'

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class Block(Component):
    template_name = 'base/components/block.html'

    def __init__(self, children: list[Component], style: str = None):
        self.children = children
        if style:
            self.style = f'block-{style}'
        else:
            self.style = 'block'

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }

    @property
    def media(self):
        return Media(
            css = {'all': ('base/css/block.css',)}
        )


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
            css = {'all': ('base/css/heading.css',)}
        )


class Paragraph(Component):
    template_name = 'base/components/paragraph.html'

    def __init__(self, text: str, style: str = None):
        self.text = text
        
        if style:
            self.style = f'paragraph-{style}'
        else:
            self.style = 'paragraph'

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style
        }

    @property
    def media(self):
        return Media(
            css = {'all': ('base/css/paragraph.css',)}
        )
