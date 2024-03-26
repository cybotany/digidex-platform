from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    """
    Landing page for project. Designed to efficiently communicate
    the value proposition of the product and/or service to the target audience.
    
    Understanding Full Scope of Value Proposition:
        Who - highlight who the target audience value proposition is designed for (target audience - segment of market that can later expand in concentric circles).
        What - highlight what the pain the product and/or service solves.
        When - highlight when the pain was experienced by the target audience in the past.
        Where - highlight where the pain can or will be experienced by the target audience.
        Why - highlight why the pain is important to solve.

    Customer Pain Discovery Results:
        1. Pain does not exist
        2. Pain exists but prospect does not know
        3. Pain exists and prospect knows but have not quantified it and will do nothing about it
        4. Pain exists and prospect knows and have quantified it but will do nothing about it
        5. Pain exists and prospect knows and have quantified it and will do something about it (Most valuable customer)

    Mom Test Summary:
        1. Talk about their life instead of your idea
        2. Ask about specifics in the past instead of generics or opinions about the future
        3. Talk less and listen more

    """
    body = StreamField(
        [],
        default=[],
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
