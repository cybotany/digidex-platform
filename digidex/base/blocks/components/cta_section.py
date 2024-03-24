from base.blocks import basics as _blocks
                        

class CallToActionContent(_blocks.BaseContentBlock):
    pass


class CallToActionSection(_blocks.BaseSectionBlock):
    content = CallToActionContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_section.html'
