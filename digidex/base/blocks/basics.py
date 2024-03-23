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
    pass


class BaseGridBlock(BaseStreamBlock):
    """
    Parent:
      - BaseContent
    Child:
      - BaseBlock
    """
    pass


class BaseContentBlock(BaseStreamBlock):
    """
    Parent:
      - BaseSection
    Child:
      - BaseGrid
    """
    pass


class BaseSectionBlock(BaseStructBlock):
    """
    Parent:
      - BasePage
    Child:
      - BaseContent
    """
    pass

class SectionHeading(_blocks.BaseBlock):
    title = _blocks.BaseCharBlock(
        required=True,
        help_text="Enter the heading title"
    )
    text = _blocks.BaseTextBlock(
        required=True,
        help_text="Enter the heading text"
    )