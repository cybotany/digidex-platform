from base.blocks import basic


class NotificationIcon(basic.BasicStructBlock):
    """
    A StructBlock for individual icon links in the notification bar.
    """
    icon = basic.BasicImageBlock()
    link = basic.BasicInternalLinkBlock()
    text = basic.BasicTextBlock()

    class Meta:
        template = 'base/blocks/sections/notification/icon_block.html'
        icon = 'link'


class NotificationIconList(basic.BasicListBlock):
    """
    A ListBlock that allows for 0 to 3 _NotificationIconBlocks.
    """

    def __init__(self, **kwargs):
        super().__init__(NotificationIcon(), **kwargs)

    class Meta:
        template = 'base/blocks/sections/notification/icon_list_block.html'


class NotificationBarBlock(basic.BasicStructBlock):
    """
    A StructBlock for the notification bar.
    """
    information = basic.BasicTextBlock()
    links = NotificationIconList()

    class Meta:
        label = 'Notification Bar'
        template = 'base/blocks/sections/notification_bar.html'
        icon = 'link'
