from cms.base.blocks import composite_blocks
from cms.base.blocks import basic_blocks

class PageFooterBlock(basic_blocks.BaseStructBlock):
    logo = basic_blocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = basic_blocks.BaseTextBlock(
        required=False,
        help_text="Footer description"
    )
    links = basic_blocks.BaseListBlock(
        composite_blocks.URLBlock(label="Quick Links"),
        composite_blocks.URLBlock(label="Template Links"),
        composite_blocks.URLBlock(label="Social Links")
    )
    copyright_text = basic_blocks.BaseCharBlock(
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
