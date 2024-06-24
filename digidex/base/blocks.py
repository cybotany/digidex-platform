from wagtail.blocks import ChoiceBlock, StructBlock, CharBlock, URLBlock, StreamBlock


class TextLink(StructBlock):
    url = URLBlock(
        required=True,
        help_text="Enter the URL to link to"
    )
    text = CharBlock(
        required=True,
        help_text="Enter the text to display"
    )

    class Meta:
        icon = "link"
        label = "Link"


class HeadingBlock(StructBlock):
    subtitle = CharBlock(
        required=False
    )
    title = CharBlock(
        classname="title",
        required=True
    )
    title_size = ChoiceBlock(
        choices=[
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
        ],
        default="h2",
        required=False
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class FootnoteBlock(StructBlock):
    text = CharBlock(
        required=False
    )
    link = TextLink(
        required=True
    )

    class Meta:
        template = "base/blocks/footnote_block.html"


class ContentBlock(StreamBlock):
    pass


class Section(StructBlock):
    heading = HeadingBlock(
        required=False
    )
    content = ContentBlock(
        required=False
    )
    footnote = FootnoteBlock(
        required=False
    )

    class Meta:
        template = "base/includes/section.html"


class FeaturedAssetSection(Section):
    class Meta:
        icon = "title"
        template = "home/includes/featured_asset_section.html"


class AssetCollectionSection(Section):
    class Meta:
        icon = "title"
        template = "home/includes/asset_collection_section.html"


class AssetCategorySection(Section):
    class Meta:
        icon = "title"
        template = "home/includes/asset_category_section.html"


class Inventory(StructBlock):
    featured_asset_section = FeaturedAssetSection()
    asset_collection_section = AssetCollectionSection()
    category_section = AssetCategorySection()

    class Meta:
        icon = "title"
        template = "home/includes/inventory.html"
