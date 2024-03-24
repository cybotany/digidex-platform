from base.blocks import basics as _blocks


class PromoTag(_blocks.BaseStructBlock):
    page = _blocks.BasePageBlock(
        required=True,
        help_text="Select the page to link to for the promo"
    )
    text = _blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter the text for the promo"
    )


class HeroHeading(_blocks.HeadingBlock):
    text = _blocks.BaseTextBlock(
        required=True
    )


class HeroButtons(_blocks.BaseStructBlock):
    primary = _blocks.ButtonBlock(
        required=True,
        help_text="Primary button"
    )
    secondary = _blocks.SecondaryButtonBlock(
        required=False,
        help_text="Secondary button"
    )


class HeroCallToActionBlock(_blocks.BaseBlock):
    promo = PromoTag(required=False)
    heading = _blocks.HeadingBlock()
    buttons = HeroButtons()


class HeroFeatureLottieBlock(_blocks.LottieBlock):
    pass


class HeroGrid(_blocks.BaseGridBlock):
    blocks = _blocks.BaseStreamBlock(
        [
            ('cta', HeroCallToActionBlock()),
            ('lottie', HeroFeatureLottieBlock())
        ]
    )


class HeroContent(_blocks.BaseContentBlock):
    grid = HeroGrid()


class HeroSection(_blocks.BaseSectionBlock):
    content = HeroContent()

    class Meta:
        template = "base/apps/home/hero_section.html"
