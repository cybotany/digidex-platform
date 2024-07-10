from django.urls import reverse

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkWrapperComponent,
    LinkComponent,
    IconComponent,
    TextComponent,
    CollectionComponent,
    ButtonComponent,
    NavigationComponent
)
from inventory.models import InventoryIndex


def build_category_panel(category):
    panel = LinkWrapperComponent(
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

def build_navigation_link_panel(item, style):
    panel = LinkComponent(
        url=item.url,
        text=item.name,
        style=style
    )
    return panel

def build_navigation_button_panel(user, style):
    base_style = "button"
    if style:
        primary_style = f"{style}-{base_style}-outline"
        alternate_style = f"{style}-{base_style}"
    panel = []

    if user.is_authenticated:
        button = ButtonComponent(
            text='Logout',
            url=reverse("account_logout"),
            style=primary_style
        )
        panel.append(button)
    else:
        buttons = [
            ButtonComponent(
                text='Login',
                url=reverse("account_login"),
                style=primary_style
            ),
            ButtonComponent(
                text='Signup',
                url=reverse("account_signup"),
                style=alternate_style
            )
        ]
        panel.extend(buttons)
    return panel


def build_user_navigation(user):
    style = 'nav'
    links = []
    buttons = []

    inventory = InventoryIndex.objects.get(owner=user)

    party = inventory.get_party()
    if party:
        party_items = party.get_items()
        for item in party_items:
            links.append(build_navigation_link_panel(item, style))

    buttons.extend(build_navigation_button_panel(user, style))

    panel = NavigationComponent(
        links=links,
        buttons=buttons
    )
    return panel
