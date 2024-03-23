from base.blocks import basic_blocks, composite_blocks

class LogoLinkBlock(basic_blocks.BaseStructBlock):
    logo_image = basic_blocks.BaseImageBlock(
        required=True,
        help_text="Select the logo image"
    )
    url = basic_blocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL the logo should link to"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/logo_link.html'


class NavigationMenuMobileBlock(basic_blocks.BaseStructBlock):
    nav_links = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock(help_text="Add navigation links")
    )
    mobile_nav_buttons = basic_blocks.BaseListBlock(
        composite_blocks.ButtonBlock(),
        help_text="Add navigation buttons"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_mobile.html'


class ShoppingCartBlock(composite_blocks.ButtonBlock):
    pass

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/shopping_cart.html'


class NavigationMenuDesktopBlock(basic_blocks.BaseStructBlock):
    desktop_nav_buttons = basic_blocks.BaseListBlock(
        composite_blocks.ButtonBlock(),
        help_text="Add navigation buttons"
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/menu_desktop.html'


class NavigationBarBlock(basic_blocks.BaseStructBlock):
    nav_menu = NavigationMenuMobileBlock()
    desktop_buttons = NavigationMenuDesktopBlock()

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/navigation_bar.html'
