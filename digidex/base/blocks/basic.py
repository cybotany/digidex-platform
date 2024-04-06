from wagtail import blocks
from wagtail.images import blocks as image_blocks
from wagtail.documents import blocks as doc_blocks

class BasicStructBlock(blocks.StructBlock):
    """
    Used internally
    """
    pass


class BasicIntegerBlock(blocks.IntegerBlock):
    """
    Used internally
    """
    pass


class BasicFloatBlock(blocks.FloatBlock):
    """
    Used internally
    """
    pass


class BasicChoiceBlock(blocks.ChoiceBlock):
    """
    Used internally
    """
    pass


class BasicListBlock(blocks.ListBlock):
    """
    Used internally
    """
    pass


class BasicBooleanBlock(blocks.BooleanBlock):
    """
    Used internally
    """
    pass


class BasicCharBlock(blocks.CharBlock):
    """
    Used internally
    """
    pass


class BasicImageBlock(image_blocks.ImageChooserBlock):
    """
    Used internally
    """
    pass


class BasicDocumentBlock(doc_blocks.DocumentChooserBlock):
    """
    Used internally
    """
    pass


class BasicHeadingBlock(BasicStructBlock):
    """
    Used internally
    """
    text = blocks.CharBlock(
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
            ("h6", "H6"),
        ],
        blank=True,
        required=False
    )
    style = blocks.CharBlock(
        default="heading",
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class BasicParagraphBlock(BasicStructBlock):
    """
    Used internally
    """
    text = blocks.TextBlock(
        required=True
    )
    style = blocks.CharBlock(
        default="paragraph",
        required=False,
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class BasicIconBlock(BasicStructBlock):
    """
    Used internally
    """
    icon = BasicImageBlock(
        required=True,
        help_text="Select an icon for the info block"
    )
    style = blocks.CharBlock(
        blank=True,
        default="icon",
        required=False
    )

    class Meta:
        template = 'base/blocks/icon_block.html'
        icon = 'image'
        label = 'Icon'


class BasicInternalLinkBlock(BasicStructBlock):
    """
    Used internally
    """
    page = blocks.PageChooserBlock(
        required=False,
        help_text="Select an internal page to link to."
    )
    style = blocks.CharBlock(
        blank=True,
        default="link",
        required=False
    )

    class Meta:
        icon = 'link'
        label = 'Internal Page Link'


class BasicExternalLinkBlock(BasicStructBlock):
    """
    Used internally
    """
    url = blocks.URLBlock(
        required=False,
        help_text="Select an external URL to link to."
    )
    style = blocks.CharBlock(
        blank=True,
        default="link",
        required=False
    )

    class Meta:
        icon = 'link'
        label = 'External URL Link'


class BasicTextBlock(BasicStructBlock):
    """
    Used internally
    """
    text = blocks.CharBlock(
        required=True
    )
    style = blocks.CharBlock(
        blank=True,
        default="text",
        required=False
    )

    class Meta:
        template = 'base/blocks/text_block.html'


class BasicButton(BasicStructBlock):
    """
    Used internally
    """
    page = BasicInternalLinkBlock()
    text = BasicTextBlock()
    style = blocks.CharBlock(
        blank=True,
        default="text",
        required=False
    )


class BasicButtonBlock(BasicButton):
    """
    Used internally
    """
    class Meta:
        template = 'base/blocks/button_block.html'


class BasicIconButtonBlock(BasicButton):
    """
    Used internally
    """
    icon = BasicIconBlock(
        required=True
    )
    
    class Meta:
        template = 'base/blocks/icon_button_block.html'


class BasicFigureBlock(BasicStructBlock):
    """
    Used internally
     """
    image = BasicImageBlock(
        required=True
    )
    caption = BasicCharBlock(
        required=False
    )
    attribution = BasicCharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/figure_block.html"


class BasicStreamBlock(blocks.StreamBlock):
    """
    Used internally
    """
    heading = BasicHeadingBlock()
    paragraph = BasicParagraphBlock()
    button = BasicButtonBlock()
    icon_button = BasicIconButtonBlock()
