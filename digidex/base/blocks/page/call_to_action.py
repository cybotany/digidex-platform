from base.blocks import basics as _blocks
                        

class CallToActionContentBlock(_blocks.BaseContentBlock):
    pass


class CallToActionSectionBlock(_blocks.BaseSectionBlock):
    content = CallToActionContentBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
