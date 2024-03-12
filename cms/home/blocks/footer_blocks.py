from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class FooterBlock(blocks.StructBlock):
    logo = basic_blocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = blocks.TextBlock(
        required=False,
        help_text="Footer description"
    )
    quick_links = blocks.ListBlock(
        basic_blocks.BaseURLBlock(label="Quick Link")
    )
    template_links = blocks.ListBlock(
        basic_blocks.BaseURLBlock(label="Template Link")
    )
    social_links = blocks.ListBlock(
        basic_blocks.BaseURLBlock(label="Social Link")
    )
    copyright_text = basic_blocks.BaseCharBlock(
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
