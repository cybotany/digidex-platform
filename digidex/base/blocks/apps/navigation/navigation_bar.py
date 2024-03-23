from base.blocks import basic, component


class LogoLinkBlock(basic.BaseStructBlock):
    logo_image = basic.BaseImageBlock(
        required=True,
        help_text="Select the logo image"
    )
    url = basic.BaseURLBlock(
        required=True,
        help_text="Enter the URL the logo should link to"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/logo_link.html'


class NavigationMenuMobileBlock(basic.BaseStructBlock):
    nav_links = basic.BaseListBlock(
        component.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = basic.BaseListBlock(
        component.ButtonBlock(),
        help_text="Add navigation buttons"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_mobile.html'


class ShoppingCartBlock(component.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(basic.BaseStructBlock):
    desktop_nav_buttons = basic.BaseListBlock(
        component.ButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_desktop.html'


class NavigationBarBlock(basic.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/navigation_bar.html'
