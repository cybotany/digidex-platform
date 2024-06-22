from wagtail.blocks import StructBlock, CharBlock, TextBlock, URLBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock


class LinkBlock(StructBlock):
    link = URLBlock(
        required=True,
        help_text="Enter the URL to link to"
    )
    text = CharBlock(
        required=True,
        help_text="Enter the text to display"
    )

    class Meta:
        icon = "link"
        label = "URL"


class ImageLinkBlock(StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text="Select an image to use"
    )
    url = LinkBlock(
        required=True
    )


class NotificationBlock(StructBlock):
    message = CharBlock(
        required=True
    )
    icons = ListBlock(
        ImageLinkBlock(),
        required=False
    )

    class Meta:
        template = 'base/blocks/notification.html'
        icon = "notification"
        label = "Notification"


class NavigationBlock(StructBlock):
    logo = ImageChooserBlock(
        required=True
    )
    links = ListBlock(
        URLBlock()
    )
    login_link = URLBlock(
        required=True
    )
    get_started_link = URLBlock(
        required=True
    )


class HeaderBlock(StructBlock):
    heading = CharBlock(
        required=True
    )
    subheading = TextBlock(
        required=False
    )


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
