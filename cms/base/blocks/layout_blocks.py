from base.blocks import basic_blocks as bblocks
from base.blocks import composite_blocks as cblocks

class BaseBlock(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/layout/block.html"


class BaseGrid(bblocks.BaseStreamBlock):
    items = bblocks.BaseStreamBlock(
        [
            ('base_block', BaseBlock()),
        ],
        min_num=1
    )
    class Meta:
        template = "blocks/layout/grid.html"


class BaseContent(bblocks.BaseStructBlock):
    content_block = bblocks.BaseStreamBlock(
        [
            ('grid', BaseGrid()),
            ('block', BaseBlock()),
        ],
        max_num=1
    )
    class Meta:
        template = "blocks/layout/content.html"


class BaseSection(bblocks.BaseStructBlock):
    content = BaseContent()
    class Meta:
        template = "blocks/layout/section.html"


class BasePageBody(bblocks.BaseStreamBlock):
    sections = bblocks.BaseStreamBlock(
        [
            ('section', BaseSection()),
        ],
        min_num=1
    ) 
    class Meta:
        template = "blocks/layout/page_body.html"


class BasePageHeader(bblocks.BaseStructBlock):
    navigation = cblocks.NavbarBlock()
    class Meta:
        template = "blocks/layout/page_header.html"


class BasePageFooter(bblocks.BaseStructBlock):
    pass
    class Meta:
        template = "blocks/layout/page_footer.html"


class BasePage(bblocks.BaseStructBlock):
    page_header = BasePageHeader()
    page_body = BasePageBody()
    page_footer = BasePageFooter()
    class Meta:
        template = "blocks/layout/page.html"
