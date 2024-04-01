from wagtail import blocks

from base import blocks as _blocks


class ListItemBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255, help_text="List item text")


class SolutionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255, help_text="Solution heading")
    description = blocks.RichTextBlock(required=True, help_text="Solution description")
    list_items = blocks.ListBlock(ListItemBlock(), help_text="List of items for the solution")


class FeatureBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255, help_text="Feature heading")
    paragraph = blocks.RichTextBlock(required=True, help_text="Feature description")


class SolutionsStreamBlock(_blocks.BaseStreamBlock):
    pass


class FeaturesStreamBlock(_blocks.BaseStreamBlock):
    pass
