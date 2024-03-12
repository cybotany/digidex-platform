from base.blocks.basic import basic_blocks as _bblocks

class ImageBlock(_bblocks.BaseStructBlock):
    image = _bblocks.BaseImageBlock()
    caption = _bblocks.BaseCharBlock(
        required=False
    )
    attribution = _bblocks.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        label = "Image"
        template = "blocks/image_block.html"


class URLBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=False,
        help_text="Optional: Select an icon image"
    )
    text = _bblocks.BaseTextBlock(
        help_text="Enter the link title"
    )
    url = _bblocks.BaseURLBlock(
        required=True,
        help_text="Enter the URL"
    )
    target = _bblocks.BaseChoiceBlock(
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


class ButtonBlock(_bblocks.BaseStructBlock):
    button = URLBlock()

    class Meta:
        icon = 'plus'
        template = 'blocks/button_block.html'


class HeadingBlock(_bblocks.BaseStructBlock):
    heading = _bblocks.BaseCharBlock(
        help_text="Enter the title"
    )
    subtitle = _bblocks.BaseCharBlock(
        required=False,
        help_text="Enter the subtitle (optional)"
    )

    class Meta:
        icon = 'title'
        label = 'Heading'
        template = 'blocks/section_heading.html'


class TextContentBlock(_bblocks.BaseStructBlock):
    heading = HeadingBlock()
    body = _bblocks.BaseTextBlock(
        help_text="Enter the section body text"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'
