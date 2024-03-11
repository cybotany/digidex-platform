from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TopBarBlock(blocks.StructBlock):
    promo = TopBarPromoBlock(
        help_text="Set the promotional message for the top bar"
    )
    links = blocks.ListBlock(
        TopBarLinkBlock(help_text="Add links to the top bar")
    )

    class Meta:
        icon = 'edit'
        template = 'blocks/top_bar_block.html'
