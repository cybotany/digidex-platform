from wagtail import blocks
from wagtail.embeds import blocks as embed_blocks
from wagtail.images import blocks as img_blocks


class LinkPageBlock(blocks.PageChooserBlock):
    class Meta:
        icon = "link"
        template = "base/blocks/link_block.html"


class LinkURLBlock(blocks.URLBlock):
    class Meta:
        icon = "link"
        template = "base/blocks/link_block.html"


class HeadingBlock(blocks.CharBlock):
    heading_text = blocks.CharBlock(
        classname="title",
        required=True
    )
    size = blocks.ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        blank=True,
        required=False,
    )
    css_style = blocks.ChoiceBlock(
        choices=[
            ("heading", "Select a style (optional)"),
            ("heading-hero", "Hero Section"),
            ("heading-features", "Features Section"),
            ("heading-accordion", "FAQ Accordion Section"),
            ("heading-footer", "Footer Section"),
            ("heading-review", "Review Section"),
            ("heading-top", "Page Heading Section"),
            ("heading-solution", "Solution Section"),
            ("heading-solution-large", "Large Solution Section"),
            ("heading-post", "Blog Post Section"),
            ("heading-about", "About Us Section"),
            ("heading-account", "Account Login Section"),
            ("heading-description", "Product Description Section"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class ParagraphBlock(blocks.RichTextBlock):
    content = blocks.RichTextBlock()
    css_style = blocks.ChoiceBlock(
        choices=[
            ("paragraph", "Select a style (optional)"),
            ("paragraph-hero", "Hero Section"),
            ("paragraph-features", "Features Section"),
            ("paragraph-accordion", "FAQ Accordion Section"),
            ("paragraph-footer", "Footer Section"),
            ("paragraph-review", "Review Section"),
            ("paragraph-top", "Page Heading Section"),
            ("paragraph-solution", "Solution Section"),
            ("paragraph-solution-large", "Large Solution Section"),
            ("paragraph-post", "Blog Post Section"),
            ("paragraph-about", "About Us Section"),
            ("paragraph-account", "Account Login Section"),
            ("paragraph-description", "Product Description Section"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "link"
        template = "base/blocks/paragraph_block.html"


class ImageBlock(blocks.StructBlock):
    image = img_blocks.ImageChooserBlock(
        required=True
    )
    caption = blocks.CharBlock(
        required=False
    )
    attribution = blocks.CharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"
