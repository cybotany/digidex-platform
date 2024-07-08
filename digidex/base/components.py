from dataclasses import dataclass, asdict

from laces.components import Component


@dataclass
class SectionComponent(Component):

    children: list[Component]
    style: str = 'section'
    template_name: str = "base/components/section.html"

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class BlockComponent(Component):

    children: list[Component]
    style: str = 'block'
    template_name: str = 'base/components/block.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class HeadingComponent(Component):

    text: str
    size: int = 2
    style: str = 'heading'
    template_name: str = 'base/components/heading.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class ParagraphComponent(Component):

    text: str
    style: str = 'paragraph'
    template_name: str = 'base/components/paragraph.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class LinkComponent(Component):

    url: str
    children: list[Component]
    style: str = 'link'
    template_name: str = 'base/components/link.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class IconComponent(Component):

    source: str
    alt: str
    style: str = 'icon'
    template_name: str = 'base/components/icon.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class TextComponent(Component):

    text: str
    style: str = 'text'
    template_name: str = 'base/components/text.html'

    def get_context_data(self, parent_context=None):
        return asdict(self)
