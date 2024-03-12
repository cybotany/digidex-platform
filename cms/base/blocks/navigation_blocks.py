from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class NavbarBlock(blocks.StructBlock):
    nav_links = blocks.ListBlock(
        basic_blocks.BaseURLBlock(help_text="Add navigation links")
    )
    action_buttons = blocks.ListBlock(
        basic_blocks.ButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = basic_blocks.BaseURLBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
