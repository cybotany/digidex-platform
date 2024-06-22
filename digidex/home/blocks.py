from wagtail.blocks import (
    StructBlock,
    CharBlock,
    URLBlock,
    ListBlock
)

from wagtail.images.blocks import ImageChooserBlock


class AssetBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    links = ListBlock(URLBlock())
    login_link = URLBlock(required=True)
    get_started_link = URLBlock(required=True)
    cart_icon = ImageChooserBlock(required=True)
    cart_quantity = CharBlock(required=True)


class CategoryBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    links = ListBlock(URLBlock())
    login_link = URLBlock(required=True)
    get_started_link = URLBlock(required=True)
    cart_icon = ImageChooserBlock(required=True)
    cart_quantity = CharBlock(required=True)


class HeroBlock(StructBlock):
    logo = ImageChooserBlock(required=True)
    links = ListBlock(URLBlock())
    login_link = URLBlock(required=True)
    get_started_link = URLBlock(required=True)
    cart_icon = ImageChooserBlock(required=True)
    cart_quantity = CharBlock(required=True)
