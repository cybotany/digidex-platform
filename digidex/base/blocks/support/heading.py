from base.blocks import basic_blocks as _bblocks


class ContactHeadingBlock(_bblocks.BaseStructBlock):
    heading = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )

    class Meta:
        template = 'base/blocks/support/heading.html'
