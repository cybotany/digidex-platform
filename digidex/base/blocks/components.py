from base.blocks import basics


class TagBlock(basics.BaseStructBlock):
    text = basics.BaseCharBlock(
        required=False
    )

    class Meta:
        icon = 'tag'


class URLBlock(basics.BaseStructBlock):
    text = basics.BaseCharBlock(
        required=False,
        help_text="Enter the link title"
    )
    url = basics.BaseURLBlock(
        required=False,
        help_text="Enter the URL"
    )
    target = basics.BaseChoiceBlock(
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
    icon = basics.BaseImageBlock(
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
