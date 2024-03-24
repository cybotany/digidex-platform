from base.blocks import basics as _blocks


class SupportHeadingBlock(_blocks.BaseBlock):
    heading = _blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a heading for this section."
    )
    subtitle = _blocks.BaseRichTextBlock(
        required=True,
        help_text="Enter a subtitle for this section."
    )


class SupportMethodBlock(_blocks.BaseStructBlock):
    icon = _blocks.BaseImageBlock(
        required=True
    )
    method = _blocks.BaseCharBlock(
        required=True
    )
    description = _blocks.BaseCharBlock(
        required=True
    )
    url = _blocks.BaseURLBlock(
        required=False
    )


class SupportLottieBlock(_blocks.BaseStructBlock):
    methods = _blocks.BaseListBlock(
        SupportMethodBlock(help_text="Add contact methods.")
    )


class SupportContentBlock(_blocks.BaseContentBlock):
    pass


class SupportSection(_blocks.BaseSectionBlock):
    content = SupportContentBlock()

    class Meta:
        template = 'base/blocks/support/section.html'
