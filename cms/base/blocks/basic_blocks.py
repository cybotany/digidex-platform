from wagtail import blocks
from wagtail.images import blocks as img_blocks

class BaseCharBlock(blocks.CharBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/char_block.html"
        super().__init__(*args, **kwargs)


class BaseListBlock(blocks.ListBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/list_block.html"
        super().__init__(*args, **kwargs)


class BaseChoiceBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/choice_block.html"
        super().__init__(*args, **kwargs)


class BaseFloatBlock(blocks.BaseFloatBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/float_block.html"
        super().__init__(*args, **kwargs)


class BaseBooleanBlock(blocks.BooleanBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/boolean_block.html"
        super().__init__(*args, **kwargs)


class BaseIntegerBlock(blocks.IntegerBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/integer_block.html"
        super().__init__(*args, **kwargs)


class BaseTextBlock(blocks.TextBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/text_block.html"
        super().__init__(*args, **kwargs)


class BaseURLBlock(blocks.URLBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/url_block.html"
        super().__init__(*args, **kwargs)


class BaseImageBlock(img_blocks.ImageChooserBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/url_block.html"
        super().__init__(*args, **kwargs)


class BaseStructBlock(blocks.StructBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/struct_block.html"
        super().__init__(*args, **kwargs)

    def get_template(self, context=None):
        return self.template


class BaseStructBlock(blocks.BaseStreamBlock):
    def __init__(self, *args, **kwargs):
        self.template = "blocks/base/stream_block.html"
        super().__init__(*args, **kwargs)

    def get_template(self, context=None):
        return self.template
