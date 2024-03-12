from base.blocks import basic_blocks as bblocks

class ImageBlock(bblocks.BaseStructBlock):
    image = bblocks.BaseImageBlock()
    caption = bblocks.BaseCharBlock(
        required=False
    )
    attribution = bblocks.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        label = "Image"
        template = "blocks/image_block.html"


class URLBlock(bblocks.BaseStructBlock):
    icon = bblocks.BaseImageBlock(
        required=False,
        help_text="Optional: Select an icon image"
    )
    text = bblocks.BaseTextBlock(
        help_text="Enter the link title"
    )
    url = bblocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL"
    )
    target = bblocks.BaseChoiceBlock(
        required=False,
        choices=[
            ('_self', 'Same window'),
            ('_blank', 'New window')
        ],
        help_text="Where the link should open",
        default='_self'
    )

    class Meta:
        icon = 'link'
        label = 'Enhanced URL'
        template = 'blocks/base_url_block.html'


class ButtonBlock(bblocks.BaseStructBlock):
    button = URLBlock()

    class Meta:
        icon = 'plus'
        template = 'blocks/button_block.html'


class HeadingBlock(bblocks.BaseStructBlock):
    heading = bblocks.BaseCharBlock(
        help_text="Enter the title"
    )
    subtitle = bblocks.BaseCharBlock(
        required=False,
        help_text="Enter the subtitle (optional)"
    )

    class Meta:
        icon = 'title'
        label = 'Heading'
        template = 'blocks/section_heading.html'


class TextContentBlock(bblocks.BaseStructBlock):
    heading = HeadingBlock()
    body = bblocks.BaseTextBlock(
        help_text="Enter the section body text"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'


class PromoBarBlock(bblocks.BaseStructBlock):
    message = bblocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )
    icons = bblocks.BaseListBlock(
        URLBlock(help_text="Add links to the top bar")
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_block.html'


class NavigationBarBlock(bblocks.BaseStructBlock):
    nav_links = bblocks.BaseListBlock(
        URLBlock(help_text="Add navigation links")
    )
    action_buttons = bblocks.BaseListBlock(
        ButtonBlock(help_text="Add action buttons")
    )
    shopping_cart = URLBlock()

    class Meta:
        icon = 'site'
        template = 'blocks/navbar_block.html'


class FooterBlock(bblocks.BaseStructBlock):
    logo = bblocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = bblocks.BaseTextBlock(
        required=False,
        help_text="Footer description"
    )
    links = bblocks.BaseListBlock(
        bblocks.BaseURLBlock(label="Quick Links"),
        bblocks.BaseURLBlock(label="Template Links"),
        bblocks.BaseURLBlock(label="Social Links")
    )
    copyright_text = bblocks.BaseCharBlock(
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
