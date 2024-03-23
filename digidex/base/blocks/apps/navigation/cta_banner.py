from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks
                        
class CallToActionBannerBlock(_bblocks.SectionBlock):
    title = _bblocks.BaseCharBlock()
    button = _cblocks.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
