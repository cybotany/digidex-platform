from base.blocks import basics as _blocks
from base.blocks.components import heading as _heading


class SupportContactBlock(_blocks.BaseStructBlock):
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


class SupportLottie(_blocks.BaseStructBlock):
    methods = _blocks.BaseListBlock(
        SupportContactBlock(help_text="Add contact methods.")
    )


class SupportContent(_blocks.BaseContentBlock):
    blocks = _blocks.BaseStreamBlock(
        [
            ('heading', _heading.HeadingBlock()),
            ('lottie', SupportLottie()),
        ],
        required=False
    )


class SupportSection(_blocks.BaseSectionBlock):
    content = SupportContent()

    class Meta:
        template = 'base/blocks/support/section.html'
