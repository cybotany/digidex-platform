# base/blocks/digit_block.py
from wagtail import blocks

DIGIT_STYLE_CHOICES = (
    ('white', 'White'),
    ('background', 'Background'),
    ('border', 'Border'),
    ('heading-color', 'Heading'),
    ('accent-a1', 'Accent A1'),
    ('accent-a2', 'Accent A2'),
    ('accent-a3', 'Accent A3'),
    ('accent-a4', 'Accent A4'),
    ('accent-b1', 'Accent B1'),
    ('accent-b2', 'Accent B2'),
    ('accent-b3', 'Accent B3'),
    ('paragraph-color', 'Paragraph'),
)

class _DigitBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=DIGIT_STYLE_CHOICES, default='white', help_text='Select a color scheme')
    title = blocks.CharBlock(required=True, help_text="Enter the title")
    subtitle = blocks.CharBlock(required=False, help_text="Enter the subtitle")


class DigitBlock(blocks.StreamBlock):
    digits = blocks.ListBlock(_DigitBlock())

    class Meta:
        template = "base/blocks/content/digit_block.html"
