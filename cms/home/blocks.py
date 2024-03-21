from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class HeroBlock(_lblocks.BaseBlock):
    heading = _bblocks.BaseCharBlock(
        required=True,
        max_length=75,
    )
    text = _bblocks.BaseCharBlock(
        required=False,
        max_length=150,
    )
    call_to_action = _cblocks.ButtonBlock(
        required=True
    )

    class Meta:
        label = "Hero Heading and CTA"
        template = 'home/blocks/hero_block.html'


class LottieFeature(_bblocks.BaseStructBlock):
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
        required=True
    )
    text = _bblocks.BaseCharBlock(
        required=True
    )

    class Meta:
        label = "Hero Lottie Feature"
        template = 'home/blocks/hero_feature.html'


class HeroLottie(_lblocks.BaseBlock):
    lottie_features = _bblocks.BaseListBlock(
        LottieFeature(),
        max_length=4
    )

    class Meta:
        label = "Hero Lottie Animation"
        template = 'home/blocks/hero_lottie.html'


class HeroGrid(_lblocks.GridBlock):
    items = _bblocks.BaseStreamBlock(
        [
            ('block', HeroBlock()),
            ('lottie', HeroLottie()),
        ],
        min_num=1
    )

    class Meta:
        label = "Hero Grid"
        template = 'home/blocks/hero_grid.html'


class HeroSection(_lblocks.SectionBlock):
    content = HeroGrid()

    class Meta:
        label = "Hero Section"
        template = 'home/blocks/hero_section.html'