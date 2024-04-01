from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class BaseStructBlock(blocks.StructBlock):
    pass


class BaseStreamBlock(blocks.StreamBlock):
    pass


class LogoBlock(BaseStructBlock):
    logo = ImageChooserBlock(
        required=True
    )
    alt_text = blocks.CharBlock(
        required=False
    )
    home = blocks.PageChooserBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/logo_block.html"


class LinkBlock(BaseStructBlock):
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="List item text"
    )
    url = blocks.URLBlock()


class ButtonBlock(BaseStructBlock):
    link = LinkBlock()
    button_style = blocks.ChoiceBlock(
        required=True,
        choices=[
            ('nav-button-outline', 'Outline'),
            ('nav-button', 'Filled'),
        ],
        default='nav-button',
        help_text="Button style"
    )

    class Meta:
        icon = "link"
        template = "base/blocks/button_block.html"


class ButtonCollectionBlock(BaseStreamBlock):
    button = ButtonBlock()

    class Meta:
        icon = "list-ul"
        template = "base/blocks/button_collection_block.html"


class IconBlock(BaseStructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text="Select an icon image"
    )
    url = blocks.URLBlock(
        required=True,
        help_text="Destination URL for the icon"
    )
    alt_text = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Alt text for the icon"
    )

    class Meta:
        icon = "image"
        template = "base/blocks/icon_block.html"


class IconCollectionBlock(BaseStreamBlock):
    icon = IconBlock()

    class Meta:
        icon = "list-ul"
        template = "base/blocks/icon_collection_block.html"


class HeadingBlock(BaseStructBlock):
    title = blocks.CharBlock(
        classname="title",
        required=True
    )
    size = blocks.ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class BaseListItemBlock(BaseStructBlock):
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="List item text"
    )


class BaseListBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(BaseListItemBlock(), **kwargs)

    class Meta:
        icon = 'list-ul'
        template = 'base/blocks/list_block.html'


class QuoteBlock(BaseStructBlock):
    text = blocks.TextBlock(
        required=True,
        label="Quote Text"
    )
    author = blocks.CharBlock(
        required=False,
        label="Author"
    )

    class Meta:
        icon = "openquote"
        template = "base/blocks/quote_block.html"


class CallToActionBlock(BaseStructBlock):
    link = LinkBlock()
    button_style = blocks.ChoiceBlock(
        required=False,
        choices=[
            ('btn-primary', 'Primary'),
            ('btn-secondary', 'Secondary'),
            ('btn-success', 'Success'),
            ('btn-danger', 'Danger'),
        ],
        label="Button Style",
        help_text="The appearance of the button"
    )

    class Meta:
        icon = "plus"
        template = "base/blocks/call_to_action_block.html"


class ParagraphBlock(blocks.RichTextBlock):
    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class ContentBlock(BaseStructBlock):
    """
    A generic content block for heading and body.
    """
    heading = HeadingBlock(
        max_length=50,
        help_text="Enter the heading text here"
    )
    paragraph = ParagraphBlock(
        required=False,
        help_text="Enter the body here"
    )


class ImageBlock(BaseStructBlock):
    image = ImageChooserBlock(
        required=True
    )
    caption = blocks.CharBlock(
        required=False
    )
    attribution = blocks.CharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"


class PageBodyBlock(BaseStreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    image = ImageBlock()
    embed = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

    class Meta:
        icon = "placeholder"
        template = "base/blocks/page_body_block.html"
