from base.blocks import basic_blocks

class TagBlock(basic_blocks.BaseStructBlock):
    text = basic_blocks.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = 'tag'


class URLBlock(basic_blocks.BaseStructBlock):
    text = basic_blocks.BaseCharBlock(
        required=False,
        help_text="Enter the link title"
    )
    url = basic_blocks.BaseURLBlock(
        required=False,
        help_text="Enter the URL"
    )
    target = basic_blocks.BaseChoiceBlock(
        choices=[
            ('_self', 'Same window'),
            ('_blank', 'New window')
        ],
        required=False,
        help_text="Where the link should open"
    )

    class Meta:
        icon = 'link'
        label = 'Enhanced URL'


class IconBlock(URLBlock):
    icon = basic_blocks.BaseImageBlock(
        required=False,
        help_text="Optional: Select an icon image"
    )

    class Meta:
        icon = 'link'
        label = 'Icon with Enhanced URL'


class ButtonBlock(URLBlock):
    pass

    class Meta:
        icon = 'plus'
