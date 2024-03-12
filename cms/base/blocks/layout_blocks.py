from base.blocks import basic_blocks as bblocks

class BaseBlock(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/base_block.html"


class BaseGrid(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/grid_block.html"


class BaseContent(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/content_block.html"


class BaseSectionBlock(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/section_block.html"


class BasePageBodyBlock(bblocks.BaseStreamBlock):
    pass
    class Meta:
        template = "blocks/base/layout/page_body_block.html"


class BasePageHeaderBlock(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/page_header_block.html"


class BasePageFooterBlock(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/base/layout/page_footer_block.html"
