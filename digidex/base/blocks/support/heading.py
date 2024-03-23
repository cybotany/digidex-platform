from base.blocks import basic_blocks as _bblocks


class ContactHeadingBlock(_bblocks.BaseStructBlock):
    heading = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter the heading for the solution card."
    )
    paragraph = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a descriptive paragraph for the solution."
    )

    class Meta:
        template = 'base/blocks/support/heading.html'
