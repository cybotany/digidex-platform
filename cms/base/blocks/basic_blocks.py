from wagtail import blocks
from wagtail.images import blocks as img_blocks

class BaseCharBlock(blocks.CharBlock):
    class Meta:
        template = "blocks/base/char_block.html"


class BaseListBlock(blocks.ListBlock):
    class Meta:
        template = "blocks/base/list_block.html"


class BaseChoiceBlock(blocks.ChoiceBlock):
    class Meta:
        template = "blocks/base/choice_block.html"


class BaseFloatBlock(blocks.FloatBlock):
    class Meta:
        template = "blocks/base/float_block.html"


class BaseBooleanBlock(blocks.BooleanBlock):
    class Meta:
        template = "blocks/base/boolean_block.html"


class BaseIntegerBlock(blocks.IntegerBlock):
    class Meta:
        template = "blocks/base/integer_block.html"


class BaseTextBlock(blocks.TextBlock):
    class Meta:
        template = "blocks/base/text_block.html"


class BaseURLBlock(blocks.URLBlock):
    class Meta:
        template = "blocks/base/url_block.html"


class BaseImageBlock(img_blocks.ImageChooserBlock):
    class Meta:
        template = "blocks/base/image_block.html"


class BaseStructBlock(blocks.StructBlock):
    class Meta:
        template = "blocks/base/struct_block.html"


class BaseStreamBlock(blocks.StreamBlock):
    class Meta:
        template = "blocks/base/stream_block.html"
