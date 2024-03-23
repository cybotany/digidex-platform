from base.blocks import basic, component
                        

class CallToActionBannerBlock(basic.SectionBlock):
    title = basic.BaseCharBlock()
    button = component.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
