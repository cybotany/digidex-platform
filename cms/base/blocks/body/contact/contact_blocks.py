# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class ContactMethodBlock(_bblocks.BaseStructBlock):
    contact_link = _cblocks.URLBlock()

    class Meta:
        icon = 'user'
        template = 'blocks/contact_method_block.html'


class ContactSectionBlock(_bblocks.BaseStructBlock):
    title = _cblocks.HeadingBlock()
    contact_methods = _bblocks.BaseListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )
    lottie_animation = _cblocks.LottieBlock(
        help_text="Add a Lottie animation for the section."
    )

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
