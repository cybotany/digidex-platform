from base.blocks import basics, components, layouts

class ContactHeadingBlock(basics.BaseBlock):
    heading = basics.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = basics.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )


class ContactMethodBlock(basics.BaseStructBlock):
    icon = basics.BaseImageBlock(
        required=True
    )
    method = basics.BaseCharBlock(
        required=True
    )
    description = basics.BaseCharBlock(
        required=True
    )
    url = basics.BaseURLBlock(
        required=False
    )


class ContactLottieBlock(basics.BaseStructBlock):
    methods = basics.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )


class ContactContactBlock(basics.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'


class ContactSectionBlock(basics.SectionBlock):
    title = ContactHeadingBlock()
    lottie = ContactLottieBlock()

    class Meta:
        icon = 'contact'
        template = 'base/blocks/support/section.html'
