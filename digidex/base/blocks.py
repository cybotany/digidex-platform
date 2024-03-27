# base/blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Add your heading text here")

class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "base/blocks/rich_text_block.html"

class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, help_text="Button text")
    button_url = blocks.URLBlock(required=False, help_text="Button link")
    button_style = blocks.ChoiceBlock(choices=[
        ('normal', 'Normal'),
        ('dark', 'Dark'),
        ('yellow', 'Yellow'),
        ('outline', 'Outline'),
    ], icon='cup', default='normal')

class ContentBlock(blocks.StreamBlock):
    heading = HeadingBlock()
    paragraph = RichTextBlock()
    image = ImageChooserBlock()
    button = ButtonBlock()

    class Meta:
        template = "base/blocks/content_block.html"
