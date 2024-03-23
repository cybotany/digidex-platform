from base.blocks import basic_blocks as _bblocks,\
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
        template = 'base/blocks/apps/navigation/logo_link.html'


class NavigationMenuMobileBlock(_bblocks.BaseStructBlock):
    nav_links = _bblocks.BaseListBlock(
        _cblocks.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = _bblocks.BaseListBlock(
        _cblocks.ButtonBlock(),
        help_text="Add navigation buttons"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_mobile.html'


class ShoppingCartBlock(_cblocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(_bblocks.BaseStructBlock):
    desktop_nav_buttons = _bblocks.BaseListBlock(
        _cblocks.ButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_desktop.html'


class NavigationBarBlock(_bblocks.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/navigation_bar.html'
