from cms.base.blocks import basic_blocks as _bblocks,\
                            composite_blocks as _cblocks

class NavigationLinkBlock(_cblocks.URLBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/base/page/header/navigation_bar.html'


class NavigationButtonBlock(_cblocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/base/navigation_link_block.html'


class NavigationLinkListBlock(_cblocks.URLBlock):
    nav_buttons = _bblocks.BaseListBlock(
            NavigationButtonBlock(),
            help_text="Add navigation buttons"
        )

    class Meta:
        icon = 'site'
        template = 'blocks/base/navigation_menu_block.html'


class NavigationMenuBlock(_bblocks.BaseStreamBlock):
    nav_links = _bblocks.BaseListBlock(
        _cblocks.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = NavigationLinkListBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/navigation_menu_block.html'


class NavigationDesktopBlock(_bblocks.BaseStreamBlock):
    desktop_nav_buttons = NavigationLinkListBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/navigation_menu_block.html'


class ShoppingCartBlock(_cblocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/base/navigation_bar.html'


class NavigationBarBlock(_bblocks.BaseStructBlock):
    nav_menu = NavigationMenuBlock()
    desktop_buttons = NavigationDesktopBlock()
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/navbar_block.html'
