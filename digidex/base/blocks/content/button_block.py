# base/blocks/button_block.py
from wagtail import blocks

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

class _ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255)
    url = blocks.URLBlock(required=True)
    size = blocks.ChoiceBlock(choices=BUTTON_SIZE_CHOICES, default='button', help_text="Select button size")
    style = blocks.ChoiceBlock(choices=BUTTON_STYLE_CHOICES, default='', help_text="Select button style")


class ButtonBlock(blocks.StructBlock):
    primary = _ButtonBlock()
    secondary = _ButtonBlock()

    class Meta:
        template = "base/blocks/content/button_block.html"