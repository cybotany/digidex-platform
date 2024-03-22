from base.blocks import basic_blocks as _bblocks,\
                        composite_blocks as _cblocks,\
                        layout_blocks as _lblocks

class ContactOptionBlock(_bblocks.BaseStructBlock):
    icon = _bblocks.BaseImageBlock(
        required=True
    )
    method = _bblocks.BaseCharBlock(
        required=True
    )
    detail = _bblocks.BaseCharBlock(
        required=True
    )
    link = _bblocks.BaseURLBlock(
        required=False
    )

    class Meta:
        template = 'blocks/contact_option_block.html'


class FAQBlock(_bblocks.BaseStructBlock):
    question = _bblocks.BaseCharBlock(
        required=True
    )
    answer = _bblocks.BaseTextBlock(
        required=True
    )

    class Meta:
        template = 'blocks/faq_block.html'


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

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
