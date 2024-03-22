from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class ClientLogoBlock(_bblocks.BaseStructBlock):
    logo = _bblocks.BaseImageBlock(
        required=True
    )

    class Meta:
        template = 'blocks/client_logo_block.html'
