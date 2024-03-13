from cms.base.blocks import composite_blocks
from cms.base.blocks import basic_blocks

class NavigationLinkBlock(composite_blocks.URLBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/navigation_link_block.html'


class NavigationMenuBlock(composite_blocks.URLBlock):
    nav_links = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock(help_text="Add navigation links")
    )

    class Meta:
        icon = 'site'
        template = 'blocks/navigation_menu_block.html'


class NavigationButtonBlock(composite_blocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/navigation_link_block.html'


class ShoppingCartBlock(composite_blocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/navigation_link_block.html'


class NavigationBarBlock(basic_blocks.BaseStructBlock):
    nav_menu = NavigationMenuBlock()
    action_buttons = basic_blocks.BaseStreamBlock(
        composite_blocks.ButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
