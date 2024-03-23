from base.blocks import basic_blocks as _bblocks

class ContactHeadingBlock(_bblocks.BaseBlock):
    heading = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = _bblocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )


class ContactMethodBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    method = _bblocks.BaseCharBlock(
        required=True
    )
    description = _bblocks.BaseCharBlock(
        required=True
    )
    url = _bblocks.BaseURLBlock(
        required=False
    )


class ContactLottieBlock(_bblocks.BaseStructBlock):
    methods = _bblocks.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )


class ContactContactBlock(_bblocks.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'


class ContactSectionBlock(_bblocks.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'
