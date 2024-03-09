from wagtail import blocks
from wagtail.images import blocks as i_blocks

class CategoryBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Category icon.")
    name = blocks.CharBlock(required=True, help_text="Name of the category.")
    link = blocks.URLBlock(required=True, help_text="Link to the category page.")

    class Meta:
        icon = "tag"
        template = "blocks/category_block.html"


class ProductFeatureBlock(blocks.StructBlock):
    feature_icon = i_blocks.ImageChooserBlock(
        required=True, 
        help_text="Icon representing the feature."
    )
    feature_title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Title of the feature."
    )
    feature_description = blocks.TextBlock(
        required=False,
        help_text="A short description of the feature."
    )

    class Meta:
        icon = "tick"
        template = "blocks/product_feature_block.html"


class ProductBlock(blocks.StructBlock):
    product_image = i_blocks.ImageChooserBlock(
        required=True,
        help_text="Main product image."
    )
    product_title = blocks.CharBlock(
        required=True,
        max_length=255
    )
    product_price = blocks.DecimalBlock(
        required=True,
        max_digits=10,
        decimal_places=2
    )
    product_compare_at_price = blocks.DecimalBlock(
        required=False,
        max_digits=10,
        decimal_places=2,
        help_text="Compare at price for discounts."
    )
    product_description = blocks.TextBlock(
        required=True
    )
    product_features = blocks.ListBlock(
        ProductFeatureBlock()
    )

    class Meta:
        icon = "tag"
        template = "blocks/product_block.html"


class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True, help_text="FAQ question.")
    answer = blocks.TextBlock(required=True, help_text="FAQ answer.")

    class Meta:
        icon = "help"
        template = "blocks/faq_block.html"

class FAQSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Section title, e.g., 'Frequently Asked Questions'.")
    faqs = blocks.ListBlock(FAQBlock(), help_text="Add FAQs here.")

    class Meta:
        icon = "list-ul"
        template = "blocks/faq_section_block.html"
