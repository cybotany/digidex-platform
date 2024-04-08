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


class BasicTextBlock(blocks.TextBlock):
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
    text = BasicCharBlock(
        required=True
    )
    size = BasicCharBlock(
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

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class BasicParagraphBlock(blocks.RichTextBlock):
    """
    Used internally
    """
    pass


class BasicInternalLinkBlock(blocks.PageChooserBlock):
    """
    Used internally
    """
    pass


class BasicExternalLinkBlock(blocks.URLBlock):
    """
    Used internally
    """
    pass


class BasicListBlock(blocks.ListBlock):
    """
    Used internally
    """
    pass


class BasicStreamBlock(blocks.StreamBlock):
    """
    Used internally
    """
    heading = BasicHeadingBlock()
    paragraph = BasicParagraphBlock()


class BasicButtonBlock(BasicStructBlock):
    """
    Used internally
    """
    page = BasicInternalLinkBlock()
    cta = BasicCharBlock()

    class Meta:
        template = 'base/blocks/button_block.html'


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
