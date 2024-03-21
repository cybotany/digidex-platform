from base.blocks import basic_blocks as _bblocks,\
                        layout_blocks as _lblocks


class CallToAction(_bblocks.BaseStructBlock):
    text = _bblocks.BaseCharBlock(
        required=True,
        max_length=75,
        help_text="Enter the text for the call to action."
    )
    url = _bblocks.BaseURLBlock(
        required=True,
        help_text="Enter the url for the call to action."
    )


class HeroBlock(_lblocks.BaseBlock):
    headline = _bblocks.BaseCharBlock(
        required=True,
        max_length=75,
        help_text="Enter the headline for the value proposition. Capped at 75 characters to enforce conciseness."
    )
    subheadline = _bblocks.BaseCharBlock(
        required=False,
        max_length=150,
        help_text="Enter the subheadline for the value proposition. Capped at 150 characters to enforce brevity."
    )
    cta = CallToAction()

    class Meta:
        template = 'blocks/hero_block.html'


class _LottieFeature(_bblocks.BaseStructBlock):
    order = _bblocks.BaseChoiceBlock(
        choices=[
            (1, ""),
            (2, "a2"),
            (3, "a3"),
            (4, "a4"),
        ],
        required=True,
        help_text="Select the display order and corresponding style."
    )
    icon = _bblocks.BaseImageBlock(
        required=False,
        help_text="Select an icon image for the feature."
    )
    text = _bblocks.BaseCharBlock(
        required=True,
        help_text="Enter the text for this feature."
    )

    class Meta:
        icon = 'tick'
        label = 'Feature'
        template = 'blocks/lottie/feature.html'


class HeroLottie(_lblocks.BaseBlock):
    lottie_features = _bblocks.BaseListBlock(
        _LottieFeature(),
        label="Features",
        help_text="Add up to 4 features to be displayed in the hero section.",
        max_length=4
    )

    class Meta:
        template = 'blocks/hero_lottie.html'


class HeroSection(_lblocks.SectionBlock):
    hero_block = HeroBlock()
    hero_lottie = HeroLottie()

    class Meta:
        template = 'blocks/hero_section.html'