# base/blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from .constants import COLOR_BLOCK_CHOICES

class _HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Add your text here")


class _RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "blocks/rich_text_block.html"


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=False)


class ColorBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(choices=COLOR_BLOCK_CHOICES, default='white', help_text='Select a color scheme')
    title = blocks.CharBlock(required=True, help_text="Enter the title text")
    subtitle = blocks.CharBlock(required=True, help_text="Enter the subtitle text")

    class Meta:
        template = "blocks/color/color_block.html"


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

#class CallToAction(blocks.StructBlock):
#    subtitle = blocks.CharBlock(required=True, help_text="Add your subtitle here")
#    heading = blocks.CharBlock(required=True, help_text="Add your main heading here")
#    button_text = blocks.CharBlock(required=True, help_text="Button text")
#    button_link = blocks.URLBlock(required=True, help_text="Button link")

#    class Meta:
#        template = "blocks/page/call_to_action_block.html"
#        icon = "placeholder"
#        label = "Call to Action"
