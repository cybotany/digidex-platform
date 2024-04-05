from wagtail import blocks
from wagtail.images import blocks as image_blocks

class _HeadingBlock(blocks.CharBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _SubtitleBlock(blocks.CharBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _ParagraphBlock(blocks.RichTextBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _ImageBlock(image_blocks.ImageChooserBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _BasicBlock(blocks.StructBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _GridBlock(blocks.StreamBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class _SectionBlock(blocks.StreamBlock):
    """
    Used internally for predesigned blocks
    """
    pass

class HeadingBlock(blocks.StructBlock):
    text = _HeadingBlock(
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


class SubtitleBlock(blocks.CharBlock):
    text = _SubtitleBlock()

    class Meta:
        icon = "placeholder"
        template = "base/blocks/basic/subtitle_block.html"


class ParagraphBlock(blocks.StructBlock):
    text = _ParagraphBlock(
        required=True
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/basic/paragraph_block.html"


class ImageBlock(blocks.StructBlock):
    image = _ImageBlock(
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


class BasicButtonBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        required=True
    )
    
    class Meta:
        template = 'base/blocks/basic/basic_button_block.html'
        icon = 'placeholder'
        label = 'Button'


class IconButtonBlock(blocks.StructBlock):
    icon = _ImageBlock(
        required=True
    )
    page = blocks.PageChooserBlock(
        required=True
    )
    text = blocks.CharBlock(
        required=True
    )
    
    class Meta:
        template = 'base/blocks/basic/icon_button_block.html'
        icon = 'placeholder'
        label = 'Icon Button'


class BasicBlock(_BasicBlock):
    class Meta:
        icon = "placeholder"


class GridBlock(_GridBlock):
    class Meta:
        icon = "placeholder"
        template = "base/blocks/basic/grid_block.html"


class SectionBlock(_SectionBlock):
    class Meta:
        icon = "placeholder"
        template = "base/blocks/basic/section_block.html"
