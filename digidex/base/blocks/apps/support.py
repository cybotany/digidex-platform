from base.blocks import basics as _blocks
from base.blocks.components import heading as _heading


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


class SupportContent(_blocks.BaseContentBlock):
    block = _heading.SectionHeading()


class SupportSection(_blocks.BaseSectionBlock):
    content = SupportContent()

    class Meta:
        template = 'base/blocks/support/section.html'
