from wagtail import blocks
from wagtail.embeds import blocks as _embeds
from wagtail.images import blocks as _images

class BaseStructBlock(blocks.StructBlock):
    pass


class BaseStreamBlock(blocks.StreamBlock):
    pass


class BaseImageBlock(_images.ImageChooserBlock):
    pass


class BaseURLBlock(blocks.URLBlock):
    required=False


class BasePageChooserBlock(blocks.PageChooserBlock):
    required=False


class LinkBlock(BaseStructBlock):
    internal = blocks.PageChooserBlock(
        classname="heading",
        required=False
    )
    external = blocks.URLBlock(
        classname="heading",
        required=False
    )


class ItemBlock(BaseStructBlock):
    text = blocks.CharBlock(
        required=False,
        max_length=255
    )
    link = LinkBlock(
        required=False
    )


class ButtonBlock(ItemBlock):
    pass


class IconBlock(BaseStructBlock):
    image = BaseImageBlock(
        required=True,
        help_text="Select an icon image"
    )
    item = ItemBlock()

    class Meta:
        icon = "image"


class HeadingBlock(BaseStructBlock):
    title = blocks.CharBlock(
        classname="heading",
        required=True
    )

    class Meta:
        icon = "title"


class ParagraphBlock(BaseStructBlock):
    paragraph = blocks.RichTextBlock(
        classname="paragraph",
        required=True
    )

    class Meta:
        icon = "pilcrow"


class ImageBlock(BaseStructBlock):
    image = BaseImageBlock(
        required=True
    )
    caption = blocks.CharBlock(
        required=False
    )
    attribution = blocks.CharBlock(
        required=False
    )

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"


class PageBodyBlock(BaseStreamBlock):
    heading = HeadingBlock()
    paragraph = ParagraphBlock()
    image = ImageBlock()
    embed = _embeds.EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )

    class Meta:
        icon = "placeholder"
        template = "base/blocks/page_body_block.html"
