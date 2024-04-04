from wagtail import blocks

from .constants import PREDEFINED_SUBTITLE_STYLES

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
        icon = "placeholder"
        template = "base/blocks/subtitle_block.html"
