from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class AccordionItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(
        required=True,
        max_length=255, 
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
    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Optional: Enter a title for the FAQ section."
    )
    items = blocks.ListBlock(
        AccordionItemBlock(help_text="Add FAQ items.")
    )

    class Meta:
        icon = 'list-ul'
        template = 'blocks/faq_block.html'
