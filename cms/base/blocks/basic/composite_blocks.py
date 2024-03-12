from base.blocks.basic import basic_blocks as bblocks

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
