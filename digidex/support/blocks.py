from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ContactOptionBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    method = blocks.CharBlock(required=True)
    detail = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=False)

    class Meta:
        template = 'blocks/contact_option_block.html'

class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        template = 'blocks/faq_block.html'


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
