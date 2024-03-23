from base.blocks import basic


class TagBlock(basic.BaseStructBlock):
    text = basic.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = 'tag'


class URLBlock(basic.BaseStructBlock):
    text = basic.BaseCharBlock(
        required=False,
        help_text="Enter the link title"
    )
    url = basic.BaseURLBlock(
        required=False,
        help_text="Enter the URL"
    )
    target = basic.BaseChoiceBlock(
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
    icon = basic.BaseImageBlock(
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
