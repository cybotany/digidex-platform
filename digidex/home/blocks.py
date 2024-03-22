from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class SolutionBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True)
    link_url = blocks.URLBlock(required=True)
    link_text = blocks.CharBlock(default='Learn more', required=False)
    tag = blocks.CharBlock(required=False, help_text='Optional tag like "Most popular" or "Best Value"')

    class Meta:
        template = 'blocks/solution_block.html'


class ClientLogoBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=True)

    class Meta:
        template = 'blocks/client_logo_block.html'


class ReviewBlock(blocks.StructBlock):
    review_text = blocks.TextBlock(required=True)
    reviewer_name = blocks.CharBlock(required=True, max_length=255)

    class Meta:
        template = 'blocks/review_block.html'


