from base.blocks import basics as _blocks


class CallToActionGrid(_blocks.BaseStructBlock):
    heading = _blocks.HeadingBlock()
    cta = _blocks.ButtonBlock()


class CallToActionContent(_blocks.BaseContentBlock):
    grid = CallToActionGrid()


class CallToActionSection(_blocks.BaseSectionBlock):
    content = CallToActionContent()

    class Meta:
        label = "CTA"
        icon = 'placeholder'
        template = 'base/components/sections/cta_section.html'
