from wagtail import blocks
from wagtail.images import blocks as i_blocks

class ContactMethodBlock(blocks.StructBlock):
    icon = blocks.StructBlock([
        ('image', i_blocks.ImageChooserBlock(required=True)),
        ('alt_text', blocks.CharBlock(required=False, max_length=255)),
    ])
    method_name = blocks.CharBlock(
        required=True,
        max_length=255
    )
    contact_detail = blocks.CharBlock(
        required=True,
        max_length=255
    )
    link = blocks.URLBlock(
        required=False,
        help_text="Optional: Add a link for the contact method."
    )

    class Meta:
        icon = 'user'
        template = 'blocks/contact_method_block.html'


class ContactSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=255
    )
    subtitle = blocks.CharBlock(
        required=False,
        max_length=255
    )
    contact_methods = blocks.ListBlock(
        ContactMethodBlock(help_text="Add contact methods.")
    )
    # Add Lottie animation block if needed, assuming you have a LottieBlock defined as before

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'
