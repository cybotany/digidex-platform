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


class LottieLines(blocks.BasicStructBlock):
    vertical = BasicIntegerBlock(
        required=False,
        help_text="Number of vertical lines."
    )
    horizontal = BasicIntegerBlock(
        required=False,
        help_text="Number of horizontal lines."
    )


class Animation(BasicStructBlock):
    file = BasicDocumentBlock(
        required=True
    )
    loop = BasicBooleanBlock(
        required=False
    )
    autoplay = BasicBooleanBlock(
        required=False,
        default=True
    )
    duration = BasicFloatBlock(
        required=False,
        default=0
    )
    direction = BasicChoiceBlock(
        choices=[
            (1, "Normal"),
            (-1, "Reverse")
        ],
        default=1,
        help_text="Play animation in normal or reverse direction."
    )
    renderer = BasicChoiceBlock(
        choices=[
            ("svg", "SVG"),
            ("canvas", "Canvas"),
            ("html", "HTML")
        ],
        default="svg",
        help_text="Rendering mode of the animation."
    )
    blurred = BasicBooleanBlock(
        required=False
    )


class LottieAnimation(BasicListBlock):
    """
    PLACEHOLDER
    """
    def __init__(self, **kwargs):
        super().__init__(Animation(), **kwargs)

    class Meta:
        template = 'base/blocks/animation_block.html'
