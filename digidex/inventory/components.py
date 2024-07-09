from dataclasses import dataclass, asdict
from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    TextComponent,
    CollectionComponent
)
from inventory.models import InventoryIndex


def build_category_panel(category):
    panel = LinkComponent(
        url=category.url,
        children=[
            TextComponent(
                text=category.name,
                style='category'
            ),
        ],
        style='category'
    )
    return panel

def build_categories_panel(category_collection):
    style='categories'
    children = []

    for category in category_collection:
        children.append(build_category_panel(category))
    
    collection = CollectionComponent(
        children=children,
        style=style
    )
    panel = BlockComponent(
        children=[collection,],
        style=style
    )
    return panel


def build_top_panel(user):
    style = 'top'
    inventory = InventoryIndex.objects.get(owner=user)

    block_contents = [
        HeadingComponent(
            text=inventory.__str__(),
            size=1,
            style=style
        ),
        ParagraphComponent(
            text=inventory.body,
            style=style
        ),
    ]

    categories = inventory.get_categories()
    if categories.exists():
        categories_panel = build_categories_panel(categories)
        block_contents.append(categories_panel)

    panel = SectionComponent(
        children=[
            BlockComponent(
                children=block_contents,
                style=style
            ),
        ],
        style=style
    )
    return panel
