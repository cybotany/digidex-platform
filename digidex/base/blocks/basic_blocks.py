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
    pass

class GridBlock(BaseStructBlock):
    pass

class ContentBlock(BaseStructBlock):
    pass

class SectionBlock(BaseStructBlock):
    pass
