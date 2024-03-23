from base.blocks import basic_blocks

class ContactHeadingBlock(basic_blocks.BaseBlock):
    heading = basic_blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = basic_blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )


class ContactMethodBlock(basic_blocks.BaseStructBlock):
    icon = basic_blocks.BaseImageBlock(
        required=True
    )
    method = basic_blocks.BaseCharBlock(
        required=True
    )
    description = basic_blocks.BaseCharBlock(
        required=True
    )
    url = basic_blocks.BaseURLBlock(
        required=False
    )


class ContactLottieBlock(basic_blocks.BaseStructBlock):
    methods = basic_blocks.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )


class ContactContactBlock(basic_blocks.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'


class ContactSectionBlock(basic_blocks.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'
