from wagtail import blocks
from wagtail.images import blocks as img_blocks


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
