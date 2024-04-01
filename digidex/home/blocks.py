from base import blocks as _bblocks

class InfoTagBlock(_bblocks.BaseStreamBlock):
    item = _bblocks.ItemBlock()
    icon = _bblocks.BaseImageBlock()

class HeroBlock(_bblocks.BaseStreamBlock):
    tag = InfoTagBlock()
    heading = _bblocks.HeadingBlock()
    paragraph = _bblocks.ParagraphBlock()
    buttons = _bblocks.ButtonCollectionBlock()
