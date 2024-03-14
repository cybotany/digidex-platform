from cms.base.blocks import basic_blocks as _bblocks,\
                            composite_blocks as _cblocks

class LogoLinkBlock(_bblocks.BaseStructBlock):
    logo_image = _bblocks.BaseImageBlock(
        required=True,
        help_text="Select the logo image"
    )
    url = _bblocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL the logo should link to"
    )

    class Meta:
        icon = 'site'

class NavigationLinkBlock(_cblocks.URLBlock):
    pass

    class Meta:
        icon = 'site'


class NavigationButtonBlock(_cblocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'


class NavigationLinkListBlock(_cblocks.URLBlock):
    nav_buttons = _bblocks.BaseListBlock(
            NavigationButtonBlock(),
            help_text="Add navigation buttons"
        )


class NavigationMenuBlock(_bblocks.BaseStreamBlock):
    nav_links = _bblocks.BaseListBlock(
        _cblocks.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = NavigationLinkListBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/page/header/navigation/menu.html'


class NavigationDesktopBlock(_bblocks.BaseStreamBlock):
    desktop_nav_buttons = NavigationLinkListBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/page/header/navigation/desktop_buttons.html'


class ShoppingCartBlock(_cblocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'blocks/base/page/header/navigation/shopping_cart.html'


class NavigationBarBlock(_bblocks.BaseStructBlock):
    nav_menu = NavigationMenuBlock()
    desktop_buttons = NavigationDesktopBlock()
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/base/page/header/navigation_bar.html'
