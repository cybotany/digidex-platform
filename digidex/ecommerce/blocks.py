from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class FeatureBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    text = _bblocks.BaseCharBlock(
        required=True
    )

    class Meta:
        template = 'blocks/feature_block.html'

class ProductBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    title = _bblocks.BaseCharBlock(
        required=True
    )
    description = _bblocks.BaseTextBlock(
        required=True
    )
    price = _bblocks.BaseCharBlock(
        required=True
    )
    compare_at_price = _bblocks.BaseCharBlock(
        required=False
    )
    features = _bblocks.BaseListBlock(
        FeatureBlock()
    )
    view_plan_url = _bblocks.BaseURLBlock()

    class Meta:
        template = 'blocks/product_block.html'

class FAQBlock(_bblocks.BaseStructBlock):
    question = _bblocks.BaseCharBlock(
        required=True
    )
    answer = _bblocks.BaseTextBlock(
        required=True
    )

    class Meta:
        template = 'blocks/faq_block.html'

class CategoryLinkBlock(_bblocks.BaseStructBlock):
    name = _bblocks.BaseCharBlock(
        required=True
    )
    url = _bblocks.BaseURLBlock()
    icon = _bblocks.BaseImageBlock(
        required=True
    )

    class Meta:
        template = 'blocks/category_link_block.html'
