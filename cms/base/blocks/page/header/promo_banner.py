from base.blocks.basic import basic_blocks, composite_blocks

class PromoBarBlock(basic_blocks.BaseStructBlock):
    message = basic_blocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )
    icons = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock(help_text="Add links to the top bar")
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_block.html'
