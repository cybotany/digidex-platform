from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks


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
        template = 'blocks/contact_option_block.html'


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
    link = _bblocks.BaseURLBlock(
        required=False
    )

    class Meta:
        template = 'blocks/contact_option_block.html'


class ContactLottieBlock(_bblocks.BaseStructBlock):
    pass

    class Meta:
        template = 'blocks/contact_option_block.html'


class ContactSectionBlock(_bblocks.BaseStructBlock):
    title = ContactHeadingBlock()
    methods = _bblocks.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
