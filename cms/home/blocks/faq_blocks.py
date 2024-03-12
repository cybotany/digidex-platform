from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class AccordionItemBlock(blocks.StructBlock):
    question = basic_blocks.BaseCharBlock(
        help_text="Enter the FAQ question."
    )
    answer = blocks.TextBlock(
        required=True,
        help_text="Enter the answer to the question."
    )

    class Meta:
        icon = 'question'
        template = 'blocks/accordion_item_block.html'


class FAQBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    items = blocks.ListBlock(
        AccordionItemBlock(help_text="Add FAQ items.")
    )

    class Meta:
        icon = 'list-ul'
        template = 'blocks/faq_block.html'
