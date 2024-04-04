from wagtail import blocks
from wagtail.images import blocks as image_blocks

from base.constants import PREDEFINED_HEADING_STYLES, PREDEFINED_SUBTITLE_STYLES, PREDEFINED_BLOCK_STYLES, PREDEFINED_PARAGRAPH_STYLES, PREDEFINED_GRID_STYLES, PREDEFINED_SECTION_STYLES

class NotificationIconBlock(blocks.StructBlock):
    """
    A StructBlock for individual icon links in the notification bar.
    """
    url = blocks.URLBlock(
        required=True,
        help_text="Link URL"
    )
    icon = image_blocks.ImageChooserBlock(
        required=True,
        help_text="Icon Image"
    )
    text = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text="Link Text"
    )

    class Meta:
        template = 'base/blocks/notification/icon_block.html'
        icon = 'link'
        label = 'Icon Link'


class ImageFigureBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(
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
        template = "base/blocks/image_figure_block.html"


class HeadingBlock(blocks.CharBlock):
    text = blocks.CharBlock(
        classname="title",
        required=True
    )
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_HEADING_STYLES,
        blank=True,
        required=False,
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
        template = "base/blocks/heading_block.html"


class SubtitleBlock(blocks.CharBlock):
    text = blocks.CharBlock(
        classname="title",
        required=True
    )
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_SUBTITLE_STYLES,
        blank=True,
        required=False,
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
        template = "base/blocks/heading_block.html"


class ParagraphBlock(blocks.RichTextBlock):
    text = blocks.RichTextBlock()
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_PARAGRAPH_STYLES,
        blank=True,
        required=False,
    )

    class Meta:
        icon = "pilcrow"
        template = "base/blocks/paragraph_block.html"


class BaseBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_BLOCK_STYLES,
        default='grid',
        label='Grid Style',
    )

    class Meta:
        template = 'blocks/grid_block.html'
        icon = 'grid'
        label = 'Grid'


class GridBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_GRID_STYLES,
        default='grid',
        label='Grid Style',
    )

    class Meta:
        template = 'blocks/grid_block.html'
        icon = 'grid'
        label = 'Grid'


class SectionBlock(blocks.StreamBlock):
    content = blocks.StreamBlock(
        [
            ('image', ImageFigureBlock(required=False)),
            ('grid', GridBlock(required=False)),
        ],
        icon='placeholder',
        required=False
    )
    heading_block = HeadingBlock()
    paragraph_block = ParagraphBlock()
    image_block = ImageFigureBlock()
    style = blocks.ChoiceBlock(
        choices=PREDEFINED_SECTION_STYLES,
        default='section',
        label='Section Style',
    )

    class Meta:
        icon = "doc-full"
        template = "base/blocks/section_block.html"


class PageHeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True,
        classname="full title"
    )
    introduction = blocks.RichTextBlock(
        required=False
    )

    class Meta:
        template = 'base/blocks/page_heading_block.html'
        icon = 'title'
