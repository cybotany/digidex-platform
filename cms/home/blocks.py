from base.blocks import basic_blocks as _bblocks,\
                        layout_blocks as _lblocks


class CallToAction(_bblocks.BaseStructBlock):
    text = _bblocks.BaseCharBlock(
        required=True,
        max_length=75,
    )
    url = _bblocks.BaseURLBlock(
        required=True,
    )


class HeroBlock(_lblocks.BaseBlock):
    heading = _bblocks.BaseCharBlock(
        required=True,
        max_length=75,
    )
    text = _bblocks.BaseCharBlock(
        required=False,
        max_length=150,
    )
    call_to_action = CallToAction()

    class Meta:
        template = 'blocks/hero_block.html'


class _LottieFeature(_bblocks.BaseStructBlock):
    order = _bblocks.BaseChoiceBlock(
        choices=[
            (1, "First"),
            (2, "Second"),
            (3, "Third"),
            (4, "Fourth"),
        ],
        required=True
    )
    icon = _bblocks.BaseImageBlock(
        required=False
    )
    text = _bblocks.BaseCharBlock(
        required=True
    )

    class Meta:
        icon = 'tick'
        template = 'blocks/lottie/feature.html'


class HeroLottie(_lblocks.BaseBlock):
    lottie_features = _bblocks.BaseListBlock(
        _LottieFeature(),
        max_length=4
    )

    class Meta:
        template = 'blocks/hero_lottie.html'


class HeroSection(_lblocks.SectionBlock):
    hero_block = HeroBlock()
    hero_lottie = HeroLottie()

    class Meta:
        template = 'blocks/hero_section.html'