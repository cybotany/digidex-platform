from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks

class PageFooterBlock(_bblocks.BaseStructBlock):
    logo = _bblocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = _bblocks.BaseTextBlock(
        required=False,
        help_text="Footer description"
    )
    links = _bblocks.BaseListBlock(
        _cblocks.URLBlock(label="Quick Links"),
        _cblocks.URLBlock(label="Template Links"),
        _cblocks.URLBlock(label="Social Links")
    )
    copyright_text = _bblocks.BaseCharBlock(
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'base/blocks/apps/navigation/footer_block.html'
