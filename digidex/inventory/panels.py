from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
    DateComponent,
)


class GroupPanel(Component):
    template_name = 'inventory/panels/group_panel.html'

    def __init__(self, group=dict(), current=False):
        self.url = group.get('url')
        self.icon_source = group.get('icon_source')
        self.icon_alt = group.get('icon_alt')
        self.name = group.get('name', 'No name available')
        self.current = current
        self.style = 'category'

    def get_icon_component(self):
        return IconComponent(
            source=self.icon_source,
            alt=self.icon_alt,
            style=self.style
        )

    def get_text_component(self):
        return TextComponent(
            text=self.name,
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "icon": self.get_icon_component() if self.icon_source else None,
            "text": self.get_text_component(),
            "current": self.current
        }


class GroupCollection(Component):
    template_name = 'inventory/components/group_collection.html'

    def __init__(self, groups=list()):
        self.groups = groups

    def get_current_group(self, current_group):
        return current_group.get_component(current=True)

    def get_group_collection(self):
        style = 'categories'
        return CollectionComponent(
            children=[group.get_component() for group in self.groups],
            style=style
        )

    def set_panel(self):
        panel_components = []

        if self.groups:
            current_group = self.groups.pop(0)
            panel_components.append(self.get_current_group(current_group))

            if self.groups: # Check if there are any groups left
                panel_components.append(self.get_group_collection())

        else:
            panel_components.append(EmptyComponent(asset="groups"))

        return BlockComponent(children=panel_components)

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_panel()
        }


class AssetPanel(Component):
    template_name = 'inventory/panels/asset_panel.html'

    def __init__(self, asset=dict()):
        self.heading = asset.get('heading', 'No heading available')
        self.paragraph = asset.get('paragraph', 'No paragraph available')
        self.date = asset.get('date')
        self.url = asset.get('url')
        self.thumbnail = asset.get('thumbnail')
        self.style = 'post'

    def get_heading_component(self):
        return HeadingComponent(
            text=self.heading,
            size=4,
            style=self.style
        )

    def get_paragraph_component(self):
        return ParagraphComponent(
            text=self.paragraph,
            style=self.style
        )

    def get_date_component(self):
        return DateComponent(
            date=self.date
        )

    def get_context_data(self, parent_context=None):
        return {
            "date": self.get_date_component(),
            "url": self.url,
            "heading": self.get_heading_component(),
            "paragraph": self.get_paragraph_component(),
            "thumbnail": self.thumbnail
        }
