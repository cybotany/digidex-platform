from base.blocks import basics as _blocks


class LogoLinkBlock(_blocks.BaseStructBlock):
    logo_image = _blocks.BaseImageBlock(
        required=True,
        help_text="Select the logo image"
    )
    url = _blocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL the logo should link to"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/logo_link.html'


class NavigationMenuMobileBlock(_blocks.BaseStructBlock):
    nav_links = _blocks.BaseListBlock(
        _blocks.BaseURLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = _blocks.BaseListBlock(
        _blocks.BaseButtonBlock(),
        help_text="Add navigation buttons"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_mobile.html'


class ShoppingCartBlock(_blocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(_blocks.BaseStructBlock):
    desktop_nav_buttons = _blocks.BaseListBlock(
        _blocks.BaseButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_desktop.html'


class NavigationBarBlock(_blocks.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/navigation_bar.html'
