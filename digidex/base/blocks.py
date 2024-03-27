# base/blocks.py
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

class DigitBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=DIGIT_STYLE_CHOICES, default='white', help_text='Select a color scheme')
    title = blocks.CharBlock(required=True, help_text="Enter the title")
    subtitle = blocks.CharBlock(required=False, help_text="Enter the subtitle")

class DigitDisplayBlock(blocks.StreamBlock):
    digits = blocks.ListBlock(DigitBlock())

    class Meta:
        template = "blocks/digit_display_block.html"

BUTTON_STYLE_CHOICES = (
    ('', 'Primary'),
    ('dark', 'Dark'),
    ('yellow', 'Yellow'),
    ('-outline', 'Outline'),
)

BUTTON_SIZE_CHOICES = (
    ('button', 'Primary'),
    ('button-small', 'Small'),
)

class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255)
    url = blocks.URLBlock(required=True)
    size = blocks.ChoiceBlock(choices=BUTTON_SIZE_CHOICES, default='button', help_text="Select button size")
    style = blocks.ChoiceBlock(choices=BUTTON_STYLE_CHOICES, default='', help_text="Select button style")

class ButtonDisplayBlock(blocks.StructBlock):
    primary = ButtonBlock()
    secondary = ButtonBlock()

    class Meta:
        template = "blocks/button_display_block.html"
