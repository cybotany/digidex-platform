from base.blocks import basic_blocks as _bblocks


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


class ContactLottieBlock(_bblocks.BaseStructBlock):
    methods = _bblocks.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )

    class Meta:
        template = 'base/blocks/support/lottie.html'
