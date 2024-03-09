

class CategoryPageBlock(blocks.StreamBlock):
    categories = CategoryBlock()
    featured_products = ProductBlock()
    faq_section = FAQSectionBlock()

    class Meta:
        template = "blocks/category_page_block.html"
