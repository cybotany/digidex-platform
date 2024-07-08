from dataclasses import dataclass, asdict

from laces.components import Component


@dataclass
class SectionComponent(Component):
    template_name = "base/components/section.html"

    children: list[Component]
    style: str = 'section'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class BlockComponent(Component):
    template_name = 'base/components/block.html'

    children: list[Component]
    style: str = 'block'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class HeadingComponent(Component):
    template_name = 'base/components/heading.html'

    text: str
    size: int = 2
    style: str = 'heading'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class ParagraphComponent(Component):
    template_name = 'base/components/paragraph.html'

    text: str
    style: str = 'paragraph'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class LinkComponent(Component):
    template_name = 'base/components/link.html'

    url: str
    children: list[Component]
    style: str = 'link'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class IconComponent(Component):
    template_name = 'base/components/icon.html'

    source: str
    alt: str
    style: str = 'icon'

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class TextComponent(Component):
    template_name = 'base/components/text.html'

    text: str
    style: str = 'text'

    def get_context_data(self, parent_context=None):
        return asdict(self)
