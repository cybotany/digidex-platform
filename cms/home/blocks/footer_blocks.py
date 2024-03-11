from wagtail import blocks
# Project specific blocks
from base.blocks import basic_blocks

class QuickLinkBlock(basic_blocks.BaseURLBlock):
    pass

    class Meta:
        icon = 'link'
        template = 'blocks/quick_link_block.html'

class FooterBlock(blocks.StructBlock):
    logo_image = basic_blocks.BaseImageBlock(
        required=False,
        help_text="Footer logo image"
    )
    description = blocks.TextBlock(
        required=False,
        help_text="Footer description"
    )
    quick_links = blocks.ListBlock(
        QuickLinkBlock(label="Quick Link")
    )
    template_links = blocks.ListBlock(
        QuickLinkBlock(label="Template Link")
    )
    social_links = blocks.ListBlock(
        QuickLinkBlock(label="Social Link")
    )
    copyright_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
