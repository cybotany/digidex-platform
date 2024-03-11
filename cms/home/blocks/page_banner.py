from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class BannerBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Enter the banner subtitle."
    )
    heading = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the banner heading."
    )
    button_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the button text."
    )
    button_url = blocks.URLBlock(
        required=True,
        help_text="Enter the URL for the button."
    )
    lottie_animation = basic_blocks.LottieAnimationBlock(
        help_text="Add a Lottie animation for the section."
    )

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'
