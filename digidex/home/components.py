from django.urls import reverse

from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    TextComponent,
    CollectionComponent,
    EmptyComponent,
    ButtonComponent,
)


class NotificationComponent(Component):
    template_name = 'home/components/notification.html'

    def __init__(self, user):
        self.user = user
        self.notifications = self.get_notifications()

    def get_notifications(self):
        return self.user.notifications.all()

    def get_notification_text(self, notification):
        return TextComponent(
            text=notification.message,
            style='notification'
        )

    def get_notification_link(self, notification):
        return LinkComponent(
            url=notification.url,
            text='View',
            style='notification'
        )

    def get_notification(self, notification):
        return BlockComponent(
            children=[
                self.get_notification_text(notification),
                self.get_notification_link(notification)
            ],
            style='notification'
        )

    def get_context_data(self, parent_context=None):
        return {
            "notifications": CollectionComponent(
                children=[self.get_notification(notification) for notification in self.notifications]
            )
        }


class NavigationComponent(Component):
    template_name = 'home/components/navigation.html'

    def __init__(self, user):
        self.user = user
        self.is_authenticated = user.is_authenticated

    def get_inventory(self):
        from inventory.models import InventoryPage
        return InventoryPage.objects.get(owner=self.user)

    def get_navigation_links(self):
        links = []

        if self.is_authenticated:
            inventory = self.get_inventory()
            party = inventory.get_party()

            items = party.get_items()
            for item in items:
                links.append(
                    LinkComponent(
                        url=item.url,
                        text=item.name,
                        style='nav'
                    )
                )
        return links

    def get_navigation_buttons(self):
        buttons = []

        if self.is_authenticated:
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

    def get_context_data(self, parent_context=None):
        return {
            "links": self.get_navigation_links(),
            "buttons": self.get_navigation_buttons()
        }


class HeaderComponent(Component):
    template_name = 'home/components/header.html'

    def __init__(self, header=dict()):
        self.heading = header.get('heading', 'No heading available')
        self.paragraph = header.get('paragraph')
        self.categories = header.get('categories')
        self.style = 'top'

    def get_heading_component(self):
        return HeadingComponent(
            text=self.heading,
            size=1,
            style=self.style
        )

    def get_paragraph_component(self):
        return ParagraphComponent(
            text=self.paragraph,
            style=self.style
        )

    def get_block_component(self):
        block_children = [
            self.get_heading_component(),
        ]

        if self.paragraph:
            block_children.append(self.get_paragraph_component())

        if self.categories:
            block_children.append(self.categories)

        return BlockComponent(
            children=block_children,
            style=self.style
        )

    def set_top_panel(self):
        return SectionComponent(
            children=[self.get_block_component()],
            style=self.style
        )

    def get_context_data(self, parent_context=None):
        return {
            "panel": self.set_top_panel()
        }
