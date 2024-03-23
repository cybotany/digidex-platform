from base.blocks import basics as _blocks


class HeroBlock(_blocks.BaseBlock):
    heading = _blocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    text = _blocks.BaseTextBlock(
        required=True
    )
    primary_button = _blocks.BaseButtonBlock(
        required=True
    )
    secondary_button = _blocks.BaseButtonBlock(
        required=False
    )


class HeroContentBlock(_blocks.BaseContentBlock):
    pass


class HeroSectionBlock(_blocks.BaseSectionBlock):
    content = HeroContentBlock()

    class Meta:
        template = "blocks/hero_section.html"
