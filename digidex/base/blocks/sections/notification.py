from wagtail import blocks

from base.blocks import basic

class NotificationInformation(blocks.CharBlock):
    """
    A CharBlock for text-based information in the notification bar.
    """
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('help_text', 'Enter the notification text to be displayed in the notification bar.')
        super().__init__(*args, **kwargs)

    class Meta:
        label = 'Notification Text'
        template = 'base/blocks/sections/notification/information_block.html'


class NotificationIcon(blocks.StructBlock):
    """
    A StructBlock for individual icon links in the notification bar.
    """
    url = blocks.URLBlock(
        required=True,
        help_text="Link URL"
    )
    icon = basic.Image(
        required=True,
        help_text="Icon Image"
    )
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Link Text"
    )

    class Meta:
        label = 'Icon Link'
        template = 'base/blocks/sections/notification/icon_block.html'
        icon = 'link'


class NotificationIconList(blocks.ListBlock):
    """
    A ListBlock that allows for 0 to 3 _NotificationIconBlocks.
    """

    def __init__(self, **kwargs):
        super().__init__(NotificationInformation(), **kwargs)

    class Meta:
        label = 'Icon Links'
        template = 'base/blocks/sections/notification/icon_list_block.html'


class NotificationBarBlock(blocks.StructBlock):
    """
    A StructBlock for the notification bar.
    """
    information = NotificationInformation(
        required=True,
    )
    links = NotificationIconList(
        required=False,
    )

    class Meta:
        label = 'Notification Bar'
        template = 'base/blocks/sections/notification_bar.html'
        icon = 'link'
