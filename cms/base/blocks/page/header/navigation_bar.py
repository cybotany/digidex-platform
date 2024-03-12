from base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class NavigationBarBlock(bblocks.BaseStructBlock):
    nav_links = bblocks.BaseListBlock(
        cblocks.URLBlock(help_text="Add navigation links")
    )
    action_buttons = bblocks.BaseListBlock(
        cblocks.ButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = cblocks.URLBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
