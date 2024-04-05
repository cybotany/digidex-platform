from wagtail import blocks
from wagtail.images import blocks as image_blocks

class Heading(blocks.CharBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class HeadingBlock(blocks.StructBlock):
    text = Heading(
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

    class Meta:
        icon = "title"
        template = "base/blocks/basic/heading_block.html"


class Paragraph(blocks.RichTextBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class ParagraphBlock(blocks.StructBlock):
    text = Paragraph(
        required=True
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"


class Image(image_blocks.ImageChooserBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class ImageBlock(blocks.StructBlock):
    image = Image(
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
        template = "base/blocks/basic/image_figure_block.html"


class Section(blocks.StreamBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class SectionBlock(Section):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    image = ImageBlock()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/basic/section_block.html"
        label = "Section Block"
        group = "Basic Blocks"


class Button(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    page = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        required=True
    )


class ButtonBlock(Button):
    page = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        required=True
    )
    
    class Meta:
        template = 'base/blocks/basic/button_block.html'
        icon = 'placeholder'
        label = 'Button'


class IconButtonBlock(Button):
    icon = Image(
        required=True
    )
    
    class Meta:
        template = 'base/blocks/basic/icon_button_block.html'
        icon = 'placeholder'
        label = 'Icon Button'


class PageHeading(blocks.StructBlock):
    """
    Page Heading Block
    """
    heading = Heading(
        required=True
    )
    introduction = Paragraph(
        required=False
    )


class PageHeadingBlock(PageHeading):
    """
    Page Heading Block
    """

    class Meta:
        template = 'base/blocks/sections/heading.html'
        icon = 'title'
        label = 'Page Heading'
