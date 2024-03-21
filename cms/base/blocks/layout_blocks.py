from base.blocks import basic_blocks as _bblocks

class BaseBlock(_bblocks.BaseStructBlock):
    pass


class GridBlock(_bblocks.BaseStreamBlock):
    items = _bblocks.BaseStreamBlock(
        [
            ('base_block', BaseBlock()),
        ],
        min_num=1
    )


class ContentBlock(_bblocks.BaseStructBlock):
    content_block = _bblocks.BaseStreamBlock(
        [
            ('grid', GridBlock()),
            ('block', BaseBlock()),
        ],
        max_num=1
    )


class SectionBlock(_bblocks.BaseStructBlock):
    content = ContentBlock()
