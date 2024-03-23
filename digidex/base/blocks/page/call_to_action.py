from digidex.base.blocks import layouts
from digidex.base.blocks import basics, components
                        

class CallToActionBannerBlock(layouts.SectionBlock):
    title = basics.BaseCharBlock()
    button = components.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
