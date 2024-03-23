from base.blocks import basics as _blocks
                        

class CallToActionContentBlock(_blocks.ContentBlock):
    pass


class CallToActionSectionBlock(_blocks.SectionBlock):
    content = CallToActionContentBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_banner.html'
