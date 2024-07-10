from django.urls import reverse

from laces.components import Component

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
    NavigationComponent,
)
from inventory.models import InventoryIndex


class ItemComponent(Component):
    template_name = 'inventory/components/item.html'

    def __init__(self, item):
        self.date = item.created_at
        self.url = item.url
        self.heading = HeadingComponent(
            text=item.name,
            size=4,
            style='post'
        )
        self.paragraph = ParagraphComponent(
            text=item.name,
            style='post'
        )

    def get_context_data(self, parent_context=None):
        return {
            "date": self.date,
            "url": self.url,
            "heading": self.heading,
            "paragraph": self.paragraph
        }


class CategoryComponent(Component):
    template_name = 'inventory/components/category.html'

    def __init__(self, category):
        self.url = category.url
        self.text = category.name

    def get_context_data(self, parent_context=None):
        return {
            "url": self.url,
            "text": self.text
        }


class DashboardComponent(Component):
    template_name = 'inventory/components/dashboard.html'

    def __init__(self, user):
        self.user = user
        self.inventory = InventoryIndex.objects.get(owner=user)
        self.categories = self.inventory.get_categories()
        self.party = self.inventory.get_party()
        self.panels = [
            self.get_navigation_panel(),
            self.get_top_panel()
        ]

    def get_context_data(self, parent_context=None):
        return {
            "user": self.user,
            "inventory": self.inventory,
            "categories": self.categories,
            "party": self.party
        }

    def get_navigation_panel(self):
        panel = NavigationComponent(
            links=self._get_navigation_links(),
            buttons=self._get_navigation_buttons()
        )
        return panel

    def _get_navigation_links(self):
        links = []
        items = self.party.get_items()
        for item in items:
            links.append(
                LinkComponent(
                    url=item.url,
                    text=item.name,
                    style='nav'
                )
            )
        return links

    def _get_navigation_buttons(self):
        buttons = []

        if self.user.is_authenticated:
            button = ButtonComponent(
                text='Logout',
                url=reverse("account_logout"),
                style='nav-button-outline'
            )
            buttons.append(button)
        else:
            buttons = [
                ButtonComponent(
                    text='Login',
                    url=reverse("account_login"),
                    style='nav-button-outline'
                ),
                ButtonComponent(
                    text='Signup',
                    url=reverse("account_signup"),
                    style='nav-button'
                )
            ]
            buttons.extend(buttons)
        return buttons

    def get_top_panel(self):
        style = 'top'
        
        block_contents = [
            HeadingComponent(
                text=self.inventory.__str__(),
                size=1,
                style=style
            ),
            ParagraphComponent(
                text=self.inventory.body,
                style=style
            ),
        ]

        if self.categories:
            categories = self._get_categories_panel()
            block_contents.append(categories)

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

    def _get_categories_panel(self):
        style='categories'
        cateory_components = [CategoryComponent(category) for category in self.categories()]
        categories = CollectionComponent(
            children=cateory_components,
            style=style
        )
        panel = BlockComponent(
            children=categories,
            style=style
        )
        return panel
