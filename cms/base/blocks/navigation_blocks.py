from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class NavLinkBlock(basic_blocks.BaseURLBlock):
    pass

    class Meta:
        icon = 'link'
        template = 'blocks/nav_link_block.html'


class ShoppingCartBlock(basic_blocks.BaseURLBlock):
    pass

    class Meta:
        icon = 'cart'
        template = 'blocks/shopping_cart_block.html'



class NavbarBlock(blocks.StructBlock):
    nav_links = blocks.ListBlock(
        NavLinkBlock(help_text="Add navigation links")
    )
    action_buttons = blocks.ListBlock(
        basic_blocks.ActionButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
