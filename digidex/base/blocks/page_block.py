# base/blocks/page_block.py
from wagtail import blocks

from .digit_block import DigitBlock
from .figure_block import FigureBlock
from .button_block import ButtonBlock

class PageHeading(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255)

    class Meta:
        template = "base/blocks/page_block.html"

class PageContent(blocks.StreamBlock):
    heading = blocks.CharBlock(required=False, max_length=255)
    paragraph = blocks.RichTextBlock()
    image = FigureBlock()
    buttons = ButtonBlock()
    digits = DigitBlock()
