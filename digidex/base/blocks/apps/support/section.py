from base.blocks import basic

class ContactHeadingBlock(basic.BaseBlock):
    heading = basic.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = basic.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )


class ContactMethodBlock(basic.BaseStructBlock):
    icon = basic.BaseImageBlock(
        required=True
    )
    method = basic.BaseCharBlock(
        required=True
    )
    description = basic.BaseCharBlock(
        required=True
    )
    url = basic.BaseURLBlock(
        required=False
    )


class ContactLottieBlock(basic.BaseStructBlock):
    methods = basic.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )


class ContactContactBlock(basic.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'


class ContactSectionBlock(basic.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'
