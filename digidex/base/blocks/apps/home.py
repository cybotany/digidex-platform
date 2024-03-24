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


class HeroBlock(_blocks.BaseBlock):
    heading = _blocks.BaseCharBlock(
        required=True,
        max_length=255
    )
    text = _blocks.BaseTextBlock(
        required=True
    )
    buttons = HeroButtons()
    

class HeroContent(_blocks.BaseContentBlock):
    block = HeroBlock()


class HeroSection(_blocks.BaseSectionBlock):
    content = HeroContent()

    class Meta:
        template = "base/apps/home/hero_section.html"
