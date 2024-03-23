from base.blocks import basic_blocks, composite_blocks
                        
class CallToActionBannerBlock(basic_blocks.SectionBlock):
    title = basic_blocks.BaseCharBlock()
    button = composite_blocks.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
