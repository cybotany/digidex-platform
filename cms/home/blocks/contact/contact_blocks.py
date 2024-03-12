from wagtail import blocks
# Project specific blocks
from cms.base.blocks import basic_blocks

class ContactMethodBlock(blocks.StructBlock):
    contact_link = basic_blocks.BaseURLBlock()

    class Meta:
        icon = 'user'
        template = 'blocks/contact_method_block.html'


class ContactSectionBlock(blocks.StructBlock):
    title = basic_blocks.BaseTitleBlock()
    contact_methods = blocks.ListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )
    lottie_animation = basic_blocks.LottieBlock(
        help_text="Add a Lottie animation for the section."
    )

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
