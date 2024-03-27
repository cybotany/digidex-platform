# base/blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class _HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Add your text here")


class _RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "blocks/rich_text_block.html"


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=False)


class ColorBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Enter the display text")
    background_color = blocks.CharBlock(required=True, help_text="Enter the background color hex value", default="#FFFFFF")
    text_color = blocks.CharBlock(required=False, help_text="Enter the text color hex value", default="#000000")
    class Meta:
        template = "blocks/color_block.html"


class Grid(blocks.StreamBlock):
    heading = _HeadingBlock()
    color = ColorBlock()


class PageHeading(blocks.StructBlock):
    heading = _HeadingBlock()
    text = blocks.CharBlock(required=False)

    class Meta:
        template = "blocks/page/heading_block.html"


class PageBody(blocks.StreamBlock):
    heading = _HeadingBlock()
    paragraph = _RichTextBlock()
    image = ImageChooserBlock()
    button = ButtonBlock()
    grid = Grid()

    class Meta:
        template = "blocks/page/body_block.html"

class CallToAction(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=True, help_text="Add your subtitle here")
    heading = blocks.CharBlock(required=True, help_text="Add your main heading here")
    button_text = blocks.CharBlock(required=True, help_text="Button text")
    button_link = blocks.URLBlock(required=True, help_text="Button link")

    class Meta:
        template = "blocks/page/call_to_action_block.html"
        icon = "placeholder"
        label = "Call to Action"