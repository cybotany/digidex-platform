from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class FeatureBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    text = blocks.CharBlock(required=True)

    class Meta:
        template = 'blocks/feature_block.html'

class ProductBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True)
    description = blocks.TextBlock(required=True)
    price = blocks.CharBlock(required=True)
    compare_at_price = blocks.CharBlock(required=False)
    features = blocks.ListBlock(FeatureBlock())
    view_plan_url = blocks.URLBlock()

    class Meta:
        template = 'blocks/product_block.html'

class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        template = 'blocks/faq_block.html'

class CategoryLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    url = blocks.URLBlock()
    icon = ImageChooserBlock(required=True)

    class Meta:
        template = 'blocks/category_link_block.html'
