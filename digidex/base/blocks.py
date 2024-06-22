from wagtail.blocks import (
    StructBlock,
    CharBlock,
    TextBlock,
    URLBlock,
    ListBlock
)

from wagtail.images.blocks import ImageChooserBlock


class NavigationBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    links = ListBlock(URLBlock())
    login_link = URLBlock(required=True)
    get_started_link = URLBlock(required=True)
    cart_icon = ImageChooserBlock(required=True)
    cart_quantity = CharBlock(required=True)


class NotificationBlock(StructBlock):
    heading = CharBlock(required=True)
    paragraph = TextBlock(required=True)


class HeaderBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    links = ListBlock(URLBlock())
    login_link = URLBlock(required=True)
    get_started_link = URLBlock(required=True)
    cart_icon = ImageChooserBlock(required=True)
    cart_quantity = CharBlock(required=True)


class FooterBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    description = TextBlock(required=True)
