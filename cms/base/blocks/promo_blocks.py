from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks


class PromoBlock(blocks.StructBlock):
    message = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_promo_block.html'


class TopBarBlock(blocks.StructBlock):
    promo = PromoBlock(
        help_text="Set the promotional message for the top bar"
    )
    links = blocks.ListBlock(
        basic_blocks.LinkBlock(help_text="Add links to the top bar")
    )
    class Meta:
        icon = 'edit'
        template = 'blocks/top_bar_block.html'
