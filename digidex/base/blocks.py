from wagtail import blocks

class HeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=True,
        classname="full",
        help_text="Enter the header text"
    )
    paragraph = blocks.TextBlock(
        required=False,
        classname="full",
        help_text="Enter the subtext"
    )

    class Meta:
        template = "blocks/page_heading_block.html"
        icon = "placeholder"
        label = "Header Section"
