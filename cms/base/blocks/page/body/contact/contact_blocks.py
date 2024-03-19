# Project specific blocks
from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class ContactMethodBlock(blocks.StructBlock):
    contact_link = _bblocks.BaseURLBlock()

    class Meta:
        icon = 'user'
        template = 'blocks/contact_method_block.html'


class ContactSectionBlock(blocks.StructBlock):
    title = _bblocks.BaseTitleBlock()
    contact_methods = blocks.ListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )
    lottie_animation = _bblocks.LottieBlock(
        help_text="Add a Lottie animation for the section."
    )

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
