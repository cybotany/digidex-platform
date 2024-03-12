from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class HeroSectionBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    promotional_link = basic_blocks.BaseURLBlock(
        help_text="Optional promotional link, for example, a discount or special offer."
    )
    button = blocks.ListBlock(
        basic_blocks.ButtonBlock()
    )
    lottie_animations = basic_blocks.LottieBlock(
        required=False
    )

    class Meta:
        template = 'blocks/hero_section_block.html'


class FeatureIconBlock(blocks.StructBlock):
    icon = basic_blocks.BaseURLBlock()
    content = basic_blocks.TextContentBlock()

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_icon_block.html'
