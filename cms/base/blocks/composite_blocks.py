from base.blocks import basic_blocks as _bblocks

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
        template = "blocks/basic/compositeimage_block.html"


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


class ButtonBlock(URLBlock):
    button_style = _bblocks.BaseChoiceBlock(
        choices=[
            ('outline', 'Outline'),
            ('fill', 'Fill'),
        ],
        icon='choice',
        help_text="Select the button style"
    )
    class Meta:
        icon = 'plus'
        template = 'blocks/button_block.html'


class HeadingBlock(_bblocks.BaseStructBlock):
    heading = _bblocks.BaseCharBlock(
        help_text="Enter the heading or title."
    )
    subtitle = _bblocks.BaseCharBlock(
        required=False,
        help_text="Enter the subtitle (optional)"
    )

    class Meta:
        icon = 'title'
        label = 'Heading'
        template = 'blocks/section_heading.html'


class ParagraphBlock(_bblocks.BaseStructBlock):
    paragraph = _bblocks.BaseTextBlock(
        help_text="Enter the paragraph text"
    )

    class Meta:
        icon = 'title'
        label = 'Paragraph'
        template = 'blocks/section_heading.html'
