from base.blocks import basics, components, layouts
                        

class CallToActionBlock(layouts.SectionBlock):
    text = basics.BaseCharBlock()
    button = components.ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
