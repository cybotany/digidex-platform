from wagtail import blocks
from wagtail.images import blocks as image_blocks

class BasicStructBlock(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class HeadingBlock(BasicStructBlock):
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
        default="heading",
        required=False,
        help_text="CSS class for styling"
    )

    class Meta:
        icon = "title"
        template = "base/blocks/basic/heading_block.html"


class ParagraphBlock(BasicStructBlock):
    text = blocks.TextBlock(
        required=True
    )
    classname = blocks.CharBlock(
        default="paragraph",
        required=False,
        help_text="CSS class for styling"
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"


class ImageBlock(image_blocks.ImageChooserBlock):
    """
    Used internally for predesigned blocks
    """
    pass


class ImageFigureBlock(BasicStructBlock):
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


class Button(BasicStructBlock):
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
        template = 'base/blocks/buttons/icon_button_block.html'


class BasicStreamBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    button = ButtonBlock()
    icon_button = IconButtonBlock()


class PageHeadingBlock(BasicStructBlock):
    """
    Page Heading Block
    """
    heading = HeadingBlock()
    paragraph = ParagraphBlock()

    class Meta:
        template = 'base/blocks/sections/heading.html'
        icon = 'title'
        label = 'Page Heading'
