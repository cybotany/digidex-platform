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
    lottie_animation_1_src = blocks.URLBlock(
        required=False,
        help_text="URL to the first Lottie animation JSON file."
    )
    lottie_animation_2_src = blocks.URLBlock(
        required=False,
        help_text="URL to the second Lottie animation JSON file."
    )

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'
