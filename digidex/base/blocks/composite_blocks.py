from base.blocks import basic_blocks as _bblocks

class TagBlock(_bblocks.BaseStructBlock):
    text = _bblocks.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = 'tag'


class URLBlock(_bblocks.BaseStructBlock):
    text = _bblocks.BaseCharBlock(
        required=False,
        help_text="Enter the link title"
    )
    url = _bblocks.BaseURLBlock(
        required=False,
        help_text="Enter the URL"
    )
    target = _bblocks.BaseChoiceBlock(
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
    icon = _bblocks.BaseImageBlock(
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
