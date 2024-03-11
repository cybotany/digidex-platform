from wagtail import blocks
from wagtail.images import blocks as i_blocks

class SolutionBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Select an icon for the solution")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the solution title")
    description = blocks.TextBlock(required=True, help_text="Enter the solution description")
    link_url = blocks.URLBlock(required=True, help_text="Enter the URL for 'Learn more' link")
    tag = blocks.CharBlock(required=False, max_length=255, help_text="Tag for the solution (optional)")

    class Meta:
        icon = 'solution'
        template = 'blocks/solution_block.html'


class SolutionsGridBlock(blocks.StructBlock):
    solutions = blocks.ListBlock(SolutionBlock(help_text="Add solutions to the grid"))

    class Meta:
        icon = 'grid'
        template = 'blocks/solutions_grid_block.html'


class ClientLogoBlock(blocks.StructBlock):
    logo = i_blocks.ImageChooserBlock(required=True, help_text="Select a client logo")

    class Meta:
        icon = 'image'
        template = 'blocks/client_logo_block.html'


class ClientsGridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="Title for the clients section")
    logos = blocks.ListBlock(ClientLogoBlock(help_text="Add client logos"))

    class Meta:
        icon = 'group'
        template = 'blocks/clients_grid_block.html'


class TextContentBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="Enter the section subtitle")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the section title")
    body = blocks.TextBlock(required=True, help_text="Enter the section body text")

    class Meta:
        icon = 'doc-full'
        template = 'blocks/text_content_block.html'


class StatisticItemBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=False, help_text="Icon representing the statistic")
    number = blocks.CharBlock(required=True, max_length=255, help_text="Statistic number")
    description = blocks.CharBlock(required=True, max_length=255, help_text="Statistic description")

    class Meta:
        icon = 'pick'
        template = 'blocks/statistic_item_block.html'


class StatisticsGridBlock(blocks.StructBlock):
    statistics = blocks.ListBlock(StatisticItemBlock(help_text="Add statistics"))

    class Meta:
        icon = 'grid'
        template = 'blocks/statistics_grid_block.html'


class FeaturedSectionBlock(blocks.StructBlock):
    lottie_animation = LottieAnimationBlock()
    text_content = TextContentBlock()
    statistics_grid = StatisticsGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/featured_section_block.html'


class FeatureItemBlock(blocks.StructBlock):
    icon = i_blocks.ImageChooserBlock(required=True, help_text="Select an icon for the feature")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the feature title")
    description = blocks.TextBlock(required=True, help_text="Enter the feature description")

    class Meta:
        icon = 'pick'
        template = 'blocks/feature_item_block.html'


class FeaturesGridBlock(blocks.StructBlock):
    features = blocks.ListBlock(FeatureItemBlock(help_text="Add feature items to display in a grid"))

    class Meta:
        icon = 'grid'
        template = 'blocks/features_grid_block.html'


class SectionHeadingBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="Enter the section subtitle")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the section title")

    class Meta:
        icon = 'title'
        template = 'blocks/section_heading_block.html'


class HostingFeaturesSectionBlock(blocks.StructBlock):
    heading = SectionHeadingBlock()
    features_grid = FeaturesGridBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/hosting_features_section_block.html'


class StarRatingBlock(blocks.StructBlock):
    # Assuming a maximum of 5 stars, this could be extended to be more dynamic
    stars = blocks.IntegerBlock(min_value=1, max_value=5, default=5, help_text="Number of stars for the review")

class ReviewBlock(blocks.StructBlock):
    rating = StarRatingBlock()
    review_text = blocks.TextBlock(required=True, help_text="The text of the review")
    reviewer_name = blocks.CharBlock(required=True, max_length=255, help_text="Name of the reviewer")

    class Meta:
        icon = 'edit'
        template = 'blocks/review_block.html'


class ReviewsWrapperBlock(blocks.StructBlock):
    reviews = blocks.ListBlock(ReviewBlock(help_text="Add reviews to the section"))

    class Meta:
        icon = 'group'
        template = 'blocks/reviews_wrapper_block.html'


class SectionTitleBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="Enter the section subtitle")
    title = blocks.CharBlock(required=True, max_length=255, help_text="Enter the section title")
    paragraph = blocks.TextBlock(required=False, help_text="Enter an introductory paragraph if needed")

    class Meta:
        icon = 'title'
        template = 'blocks/section_title_block.html'


class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, max_length=255, help_text="Enter the button text")
    button_link = blocks.URLBlock(required=True, help_text="Enter the URL the button will link to")

    class Meta:
        icon = 'link'
        template = 'blocks/button_block.html'


class ReviewSectionBlock(blocks.StructBlock):
    title = SectionTitleBlock()
    reviews = ReviewsWrapperBlock()
    button = ButtonBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/review_section_block.html'


class ContactMethodBlock(blocks.StructBlock):
    icon = blocks.StructBlock([
        ('image', i_blocks.ImageChooserBlock(required=True)),
        ('alt_text', blocks.CharBlock(required=False, max_length=255)),
    ])
    method_name = blocks.CharBlock(required=True, max_length=255)
    contact_detail = blocks.CharBlock(required=True, max_length=255)
    link = blocks.URLBlock(required=False, help_text="Optional: Add a link for the contact method.")

    class Meta:
        icon = 'user'
        template = 'blocks/contact_method_block.html'


class ContactSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    subtitle = blocks.CharBlock(required=False, max_length=255)
    contact_methods = blocks.ListBlock(ContactMethodBlock(help_text="Add contact methods."))
    # Add Lottie animation block if needed, assuming you have a LottieBlock defined as before

    class Meta:
        icon = 'contact'
        template = 'blocks/contact_section_block.html'


"""
class LottieAnimationBlock(blocks.StructBlock):
    animation_src = blocks.URLBlock(required=True, help_text="URL to the Lottie animation JSON file.")
    loop = blocks.BooleanBlock(required=False, default=True)
    autoplay = blocks.BooleanBlock(required=False, default=True)
    renderer = blocks.ChoiceBlock(choices=[('svg', 'SVG'), ('canvas', 'Canvas')], default='svg')

    class Meta:
        icon = 'code'
        template = 'blocks/lottie_animation_block.html'
"""

class AccordionItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True, max_length=255, help_text="Enter the FAQ question.")
    answer = blocks.TextBlock(required=True, help_text="Enter the answer to the question.")

    class Meta:
        icon = 'question'
        template = 'blocks/accordion_item_block.html'


class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="Optional: Enter a title for the FAQ section.")
    items = blocks.ListBlock(AccordionItemBlock(help_text="Add FAQ items."))

    class Meta:
        icon = 'list-ul'
        template = 'blocks/faq_block.html'


class BannerBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="Enter the banner subtitle.")
    heading = blocks.CharBlock(required=True, max_length=255, help_text="Enter the banner heading.")
    button_text = blocks.CharBlock(required=True, max_length=255, help_text="Enter the button text.")
    button_url = blocks.URLBlock(required=True, help_text="Enter the URL for the button.")
    lottie_animation_1_src = blocks.URLBlock(required=False, help_text="URL to the first Lottie animation JSON file.")
    lottie_animation_2_src = blocks.URLBlock(required=False, help_text="URL to the second Lottie animation JSON file.")

    class Meta:
        icon = 'placeholder'
        template = 'blocks/banner_block.html'


class SocialLinkBlock(blocks.StructBlock):
    icon = blocks.CharBlock(required=True, max_length=255, help_text="Icon class or image name")
    url = blocks.URLBlock(required=True, help_text="Social media URL")

    class Meta:
        icon = 'link'
        template = 'blocks/social_link_block.html'

class QuickLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="Title of the link")
    url = blocks.URLBlock(required=True, help_text="URL of the link")

    class Meta:
        icon = 'link'
        template = 'blocks/quick_link_block.html'

class FooterBlock(blocks.StructBlock):
    logo_image = i_blocks.ImageChooserBlock(required=False, help_text="Footer logo image")
    description = blocks.TextBlock(required=False, help_text="Footer description")
    quick_links = blocks.ListBlock(QuickLinkBlock(label="Quick Link"))
    template_links = blocks.ListBlock(QuickLinkBlock(label="Template Link"))
    social_links = blocks.ListBlock(SocialLinkBlock(label="Social Link"))
    copyright_text = blocks.CharBlock(required=True, max_length=255, help_text="Copyright text")

    class Meta:
        icon = 'site'
        template = 'blocks/footer_block.html'
