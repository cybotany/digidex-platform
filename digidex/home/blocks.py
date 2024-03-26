# home/blocks.py
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class SectionBlock(blocks.StructBlock):
    section_type = blocks.ChoiceBlock(choices=[
        ('company', 'Company'),
        ('contact', 'Contact'),
        ('regular', 'Regular'),
    ], default='regular', help_text="Select the type of section")
    content = blocks.StreamBlock([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    class Meta:
        template = "home/blocks/section_block.html"
