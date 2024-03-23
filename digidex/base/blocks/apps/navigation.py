from base.blocks import basics, components, layouts


class LogoLinkBlock(basics.BaseStructBlock):
    logo_image = basics.BaseImageBlock(
        required=True,
        help_text="Select the logo image"
    )
    url = basics.BaseURLBlock(
        required=True,
        help_text="Enter the URL the logo should link to"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/logo_link.html'


class NavigationMenuMobileBlock(basics.BaseStructBlock):
    nav_links = basics.BaseListBlock(
        components.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = basics.BaseListBlock(
        components.ButtonBlock(),
        help_text="Add navigation buttons"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_mobile.html'


class ShoppingCartBlock(components.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(basics.BaseStructBlock):
    desktop_nav_buttons = basics.BaseListBlock(
        components.ButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_desktop.html'


class NavigationBarBlock(basics.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/navigation_bar.html'
