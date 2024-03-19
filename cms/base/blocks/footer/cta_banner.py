from base.blocks import composite_blocks as _cblocks,\
                        layout_blocks as _lblocks
                      

class CallToActionBannerBlock(_lblocks.SectionBlock):
    title = _cblocks.HeadingBlock()
    button = _cblocks.ButtonBlock()
    lottie_animation = _cblocks.LottieBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'
