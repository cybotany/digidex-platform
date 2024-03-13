# Project specific blocks
from cms.base.blocks import layout_blocks as _lblocks
from cms.base.blocks import basic_blocks as _bblocks, composite_blocks as _cblocks

class AccordionItemBlock(_lblocks.BaseBlock):
    question = _bblocks.BaseCharBlock(
        help_text="Enter the FAQ question."
    )
    answer = _bblocks.BaseTextBlock(
        required=True,
        help_text="Enter the answer to the question."
    )

    class Meta:
        icon = 'question'
        template = 'blocks/accordion_item_block.html'


class FAQBlock(_lblocks.GridBlock):
    title = _cblocks.HeadingBlock()
    items = _bblocks.BaseListBlock(
        AccordionItemBlock(help_text="Add FAQ items.")
    )

    class Meta:
        icon = 'list-ul'
        template = 'blocks/faq_block.html'
