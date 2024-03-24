from base.blocks import basics as _blocks


class HeroButtons(_blocks.BaseStructBlock):
    primary = _blocks.ButtonBlock(
        required=True,
        help_text="Primary button"
    )
    secondary = _blocks.SecondaryButtonBlock(
        required=False,
        help_text="Secondary button"
    )

    class Meta:
        template = "blocks/button_hero.html"
        icon = "placeholder"
        label = "Hero Buttons"


class HeroBlock(_blocks.BaseBlock):
    heading = _blocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    text = _blocks.BaseTextBlock(
        required=True
    )
    buttons = HeroButtons()
    


class HeroContentBlock(_blocks.BaseContentBlock):
    hero = HeroBlock()


class HeroSection(_blocks.BaseSectionBlock):
    content = HeroContentBlock()

    class Meta:
        template = "blocks/hero_section.html"
