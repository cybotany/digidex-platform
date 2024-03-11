from wagtail import blocks
from wagtail.images import blocks as i_blocks
# Project specific blocks
from base.blocks import basic_blocks

class SocialLinkBlock(blocks.StructBlock):
    social = basic_blocks.BaseLinkBlock()

    class Meta:
        icon = 'link'
        template = 'blocks/social_link_block.html'


class QuickLinkBlock(blocks.StructBlock):
    url = basic_blocks.BaseURLBlock()
    class Meta:
        icon = 'link'
        template = 'blocks/quick_link_block.html'

class FooterBlock(blocks.StructBlock):
    logo_image = i_blocks.ImageChooserBlock(
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
        SocialLinkBlock(label="Social Link")
    )
    copyright_text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Copyright text"
    )

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
