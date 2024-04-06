from wagtail import blocks
from wagtail.images import blocks as image_blocks

class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(
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
    classname = blocks.CharBlock(
        default="paragraph",
        required=False,
        help_text="CSS class for styling"
    )

    class Meta:
        icon = "title"
        template = "base/blocks/basic/heading_block.html"


class ParagraphBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=True
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"


class BasicBlock(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class StructGrid(blocks.StreamBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class StreamGrid(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class ImageBlock(image_blocks.ImageChooserBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class ImageFigureBlock(blocks.StructBlock):
    image = ImageBlock(
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


class Button(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    page = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        required=False
    )


class ButtonBlock(Button):
    class Meta:
        template = 'base/blocks/buttons/button_block.html'


class IconButtonBlock(Button):
    icon = ImageBlock(
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
    heading = HeadingBlock(
        required=True
    )
    introduction = ParagraphBlock(
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
