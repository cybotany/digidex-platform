from base.blocks import basics as _blocks


class TopBarPromoBlock(_blocks.BaseStructBlock):
    message = _blocks.BaseCharBlock(
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'


class PromoBarBlock(_blocks.BaseSectionBlock):
    promo = TopBarPromoBlock()
    icons = _blocks.BaseListBlock(
        _blocks.BaseURLBlock()
    )

    class Meta:
        icon = 'doc-full'
        template = 'base/blocks/components/notification_section.html'
