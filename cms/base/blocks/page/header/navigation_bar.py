from base.blocks.basic import basic_blocks, composite_blocks

class NavigationBarBlock(basic_blocks.BaseStructBlock):
    nav_links = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock(help_text="Add navigation links")
    )
    action_buttons = basic_blocks.BaseListBlock(
        composite_blocks.ButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = composite_blocks.URLBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
