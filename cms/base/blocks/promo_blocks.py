from wagtail import blocks
from wagtail.images import blocks as i_blocks

class LinkBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(
        required=True,
        help_text="Select an icon for the link"
    )
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the display text for the link"
    )
    url = blocks.URLBlock(
        required=False,
        help_text="Enter a URL for the link (optional)"
    )

    class Meta:
        icon = 'link'
        template = 'blocks/top_bar_link_block.html'


class PromoBlock(blocks.StructBlock):
    message = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Enter the promotional message"
    )

    class Meta:
        icon = 'doc-full'
        template = 'blocks/top_bar_promo_block.html'


class TopBarBlock(blocks.StructBlock):
    promo = PromoBlock(
        help_text="Set the promotional message for the top bar"
    )
    links = blocks.ListBlock(
        LinkBlock(help_text="Add links to the top bar")
    )
    class Meta:
        icon = 'edit'
        template = 'blocks/top_bar_block.html'
