from base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class PromoBarBlock(bblocks.BaseStructBlock):
    message = bblocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )
    icons = bblocks.BaseListBlock(
        cblocks.URLBlock(help_text="Add links to the top bar")
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_block.html'
