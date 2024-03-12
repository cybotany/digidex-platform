from base.blocks.basic import base as _bblocks

class BaseBlock(_bblocks.BaseStructBlock):
    pass

    class Meta:
        template = "blocks/layout/block.html"

class GridBlock(_bblocks.BaseStreamBlock):
    items = _bblocks.BaseStreamBlock(
        [
            ('base_block', BaseBlock()),
        ],
        min_num=1
    )

    class Meta:
        template = "blocks/layout/grid.html"


class ContentBlock(_bblocks.BaseStructBlock):
    content_block = _bblocks.BaseStreamBlock(
        [
            ('grid', GridBlock()),
            ('block', BaseBlock()),
        ],
        max_num=1
    )

    class Meta:
        template = "blocks/layout/content.html"


class SectionBlock(_bblocks.BaseStructBlock):
    content = ContentBlock()

    class Meta:
        template = "blocks/layout/section.html"
