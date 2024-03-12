from base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class FooterBlock(bblocks.BaseStructBlock):
    logo = bblocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = bblocks.BaseTextBlock(
        required=False,
        help_text="Footer description"
    )
    links = bblocks.BaseListBlock(
        cblocks.URLBlock(label="Quick Links"),
        cblocks.URLBlock(label="Template Links"),
        cblocks.URLBlock(label="Social Links")
    )
    copyright_text = bblocks.BaseCharBlock(
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
