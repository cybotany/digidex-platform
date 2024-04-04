from wagtail import blocks

class _HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        classname="title",
        required=True
    )

class HeadingBlock(_HeadingBlock):
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
