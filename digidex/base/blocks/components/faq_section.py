from base.blocks import basics as _blocks
                        

class FAQContent(_blocks.BaseContentBlock):
    pass


class FAQSection(_blocks.BaseSectionBlock):
    content = FAQContent()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/apps/navigation/cta_section.html'
