from dataclasses import dataclass, asdict

from laces.components import Component


class SectionComponent(Component):
    template_name = "base/components/section.html"

    def __init__(self, children=list[Component], style="section"):
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class BlockComponent(Component):
    template_name = 'base/components/block.html'

    def __init__(self, children=list[Component], style='block'):
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "children": self.children,
            "style": self.style
        }


class HeadingComponent(Component):
    template_name = 'base/components/heading.html'

    def __init__(self, text, size=2, style='heading'):
        self.text = text
        self.size = size
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "size": self.size,
            "style": self.style
        }


class ParagraphComponent(Component):
    template_name = 'base/components/paragraph.html'

    def __init__(self, text, style='paragraph'):
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style
        }


class LinkComponent(Component):
    template_name = 'base/components/link.html'

    def __init__(self, url, children=list[Component], style='link'):
        self.url = url
        self.children = children
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "children": self.children,
            "style": self.style
        }


class IconComponent(Component):
    template_name = 'base/components/icon.html'

    def __init__(self, source, alt, style='icon'):
        self.source = source
        self.alt = alt
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "source": self.source,
            "alt": self.alt,
            "style": self.style
        }


class TextComponent(Component):
    template_name = 'base/components/text.html'

    def __init__(self, text, style='text'):
        self.text = text
        self.style = style

    def get_context_data(self, parent_context=None):
        return {
            "text": self.text,
            "style": self.style
        }
