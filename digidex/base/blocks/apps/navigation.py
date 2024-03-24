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


class NavigationMenuMobileBlock(_blocks.BaseStructBlock):
    nav_links = _blocks.BaseListBlock(
        _blocks.BaseURLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = _blocks.BaseListBlock(
        _blocks.BaseButtonBlock(),
        help_text="Add navigation buttons"
    )


class ShoppingCartBlock(_blocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(_blocks.BaseStructBlock):
    desktop_nav_buttons = _blocks.BaseListBlock(
        _blocks.BaseButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()


class NavigationBarBlock(_blocks.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/apps/navigation/navigation_bar.html'
