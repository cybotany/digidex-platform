from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class HeroSectionBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    subtitle = blocks.TextBlock(
        required=False,
        help_text="Subtitle or a short paragraph"
    )
    promotional_link = blocks.LinkBlock(help_text="Optional promotional link")
    buttons = blocks.ListBlock(
        basic_blocks.ActionButtonBlock(),
        help_text="Add one or more action buttons"
    )
    lottie_animations = blocks.StructBlock([
        ('animation_1', basic_blocks.LottieAnimationBlock(required=False)),
        ('animation_2', basic_blocks.LottieAnimationBlock(required=False)),
        ('animation_2_blur', basic_blocks.LottieAnimationBlock(required=False)),
    ], help_text="Lottie animations for the hero section")

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(blocks.StructBlock):
    icon = basic_blocks.BaseIconBlock()
    title = basic_blocks.BaseTitleBlock()
    description = blocks.TextBlock(
        required=True,
        help_text="Short description of the feature"
    )

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'
