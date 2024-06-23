from wagtail.blocks import StreamBlock, StructBlock, CharBlock, TextBlock, URLBlock, ListBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class LinkBlock(StructBlock):
    url = URLBlock(
        required=True,
        help_text="Enter the URL to link to"
    )
    text = CharBlock(
        required=True,
        help_text="Enter the text to display"
    )
    image = ImageChooserBlock(
        required=False,
        help_text="Select an image to use"
    )

    class Meta:
        icon = "link"
        label = "Link"


class ButtonSetBlock(StructBlock):
    primary = LinkBlock(
        required=True
    ),
    secondary = LinkBlock(
        required=True
    )


class NotificationBlock(StructBlock):
    message = CharBlock(
        required=True
    )
    links = LinkBlock(
        LinkBlock,
        required=False,
        max_num=2,
    )

    class Meta:
        template = 'base/blocks/notification.html'
        icon = "info-circle"
        label = "Notification Bar"


class NavigationBlock(StructBlock):
    logo = ImageChooserBlock(
        required=True
    )
    links = ListBlock(
        LinkBlock,
        required=False,
        max_num=5
    )
    buttons = ButtonSetBlock(
        required=True
    )

    class Meta:
        template = 'base/blocks/navigation.html'
        icon = "bars"
        label = "Navigation Bar"


class HeaderBlock(StructBlock):
    heading = CharBlock(
        required=True
    )
    subheading = TextBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/header.html'
        icon = "title"
        label = "Body Header"


class FooterBlock(StructBlock):
    image = ImageChooserBlock(
        required=True
    )
    description = TextBlock(
        required=True
    )
    copyright = CharBlock(
        required=True
    )

    class Meta:
        template = 'base/blocks/footer.html'
        label = "Body Footer"
