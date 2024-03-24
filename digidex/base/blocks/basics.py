from wagtail import blocks
from wagtail.images import blocks as img_blocks
from wagtail.documents import blocks as doc_blocks


class BaseCharBlock(blocks.CharBlock):
    pass


class BaseListBlock(blocks.ListBlock):
    pass


class BaseChoiceBlock(blocks.ChoiceBlock):
    pass


class BaseFloatBlock(blocks.FloatBlock):
    pass


class BaseBooleanBlock(blocks.BooleanBlock):
    pass


class BaseIntegerBlock(blocks.IntegerBlock):
    pass


class BaseTextBlock(blocks.TextBlock):
    pass


class BaseURLBlock(blocks.URLBlock):
    pass


class BasePageBlock(blocks.PageChooserBlock):
    pass


class BaseImageBlock(img_blocks.ImageChooserBlock):
    pass


class BaseDocumentBlock(doc_blocks.DocumentChooserBlock):
    pass


class BaseRichTextBlock(blocks.RichTextBlock):
    pass


class BaseStructBlock(blocks.StructBlock):
    pass


class BaseStreamBlock(blocks.StreamBlock):
    pass


class BaseBlock(BaseStructBlock):
    """
    Parent:
      - BaseGrid
    Child:
      - BaseComponents
    """

    class Meta:
        template = "base/basics/block.html"


class BaseGridBlock(BaseStreamBlock):
    """
    Parent:
      - BaseContent
    Child:
      - BaseBlock
    """

    class Meta:
        template = "base/basics/grid.html"


class BaseContentBlock(BaseStreamBlock):
    """
    Parent:
      - BaseSection
    Child:
      - BaseGrid
    """

    class Meta:
        template = "base/basics/content.html"


class BaseSectionBlock(BaseStructBlock):
    """
    Parent:
      - BasePage
    Child:
      - BaseContent
    """

    class Meta:
        template = "base/basics/section.html"


class ButtonBlock(BaseStructBlock):
    text = BaseCharBlock(
        required=True,
        help_text="Text for the button"
    )
    url = BaseURLBlock(
        required=True,
        help_text="URL the button will link to"
    )


class SecondaryButtonBlock(ButtonBlock):
    icon = BaseImageBlock()


class HeadingBlock(BaseBlock):
    title = BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    subtitle = BaseCharBlock(
        required=False,
        help_text="Enter the heading subtitle"
    )
    text = BaseTextBlock(
        required=False,
        help_text="Enter the heading text"
    )

    class Meta:
        icon = "placeholder"
        template = "base/components/blocks/heading_block.html"
        label = "Section Heading"


class HeadingSectionContent(BaseContentBlock):
    title = BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )


class HeadingSection(BaseSectionBlock):
    content = HeadingSectionContent()

    class Meta:
        icon = "placeholder"
        template = "base/components/sections/heading_section.html"
        label = "Page Heading"


class LottieAnimationBlock(BaseStructBlock):
    animation_type = BaseChoiceBlock(
        choices=[('lottie', 'Lottie')],
        default='lottie'
    )
    animation_src = BaseDocumentBlock(
        required=True
    )
    loop = BaseBooleanBlock(
        required=False,
        help_text="Loop animation"
    )
    direction = BaseIntegerBlock(
        default=1,
        help_text="Animation direction"
    )
    autoplay = BaseBooleanBlock(
        required=False,
        help_text="Autoplay animation"
    )
    renderer = BaseChoiceBlock(
        choices=[('svg', 'SVG')],
        default='svg'
    )
    default_duration = BaseFloatBlock(
        required=False,
        help_text="Default duration"
    )
    duration = BaseFloatBlock(
        required=False,
        help_text="Duration"
    )


class LineBlock(BaseStructBlock):
    width = BaseCharBlock(
        default="1px",
        help_text="Line width"
    )
    height = BaseCharBlock(
        default="1px",
        help_text="Line height"
    )
    css_class = BaseChoiceBlock(
        choices=[
            ('line-w', 'Width line'),
            ('line-h', 'Height line')
        ],
        default='line-w'
    )


class AnimationWrapperBlock(BaseStructBlock):
    lines_a = BaseListBlock(
        LineBlock(),
        help_text="Vertical lines configuration"
    )
    lines_b = BaseListBlock(
        LineBlock(),
        help_text="Horizontal lines configuration"
    )
    animations = BaseListBlock(
        LottieAnimationBlock(),
        help_text="List of Lottie animations"
    )

    class Meta:
        template = 'blocks/animation_wrapper_block.html'
