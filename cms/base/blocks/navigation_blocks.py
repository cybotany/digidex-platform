from wagtail import blocks
from wagtail.images import blocks as i_blocks

class NavLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the link title")
    url = blocks.URLBlock(required=True, help_text="Enter the link URL")

    class Meta:
        icon = 'link'
        template = 'blocks/nav_link_block.html'


class ActionButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the button text"
    )
    button_url = blocks.URLBlock(
        required=True,
        help_text="Enter the button URL"
    )
    button_style = blocks.ChoiceBlock(
        choices=[
            ('outline', 'Outline'),
            ('fill', 'Fill'),
        ], icon='choice', help_text="Select the button style")

    class Meta:
        icon = 'plus'
        template = 'blocks/action_button_block.html'


class ShoppingCartBlock(blocks.StructBlock):
    checkout_url = blocks.URLBlock(
        required=True,
        help_text="Enter the checkout page URL"
    )

    class Meta:
        icon = 'cart'
        template = 'blocks/shopping_cart_block.html'



class NavbarBlock(blocks.StructBlock):
    nav_links = blocks.ListBlock(
        NavLinkBlock(help_text="Add navigation links")
    )
    action_buttons = blocks.ListBlock(
        ActionButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = ShoppingCartBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'
