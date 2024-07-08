from dataclasses import dataclass, asdict
from laces.components import Component

from base.components import (
    SectionComponent,
    BlockComponent,
    HeadingComponent,
    ParagraphComponent,
    LinkComponent,
    IconComponent,
    TextComponent
)
from inventory.models import UserProfile


@dataclass
class Dashboard(Component):
    template_name: str = 'inventory/components/dashboard.html'

    panels: list = None

    @classmethod
    def from_user(cls, user):
        user_profile = UserProfile.objects.select_related('inventory').get(user__id=user.id)
        user_inventory = user_profile.inventory
        user_categories = user_inventory.get_children().filter(_type='c')

        if not user_categories.exists():
            pass

        heading_section = SectionComponent(
            children=[
                BlockComponent(
                    children = [
                        HeadingComponent(
                            text=user_inventory.__str__(),
                            size=1,
                            style='heading-top'
                        ),
                        ParagraphComponent(
                            text=user_profile.__str__(),
                            style='paragraph-top'
                        ),
                    ],
                    style='block-top'
                )
            ],
            style='section-top'
        )
        
        return cls(
            panels=[heading_section]
        )

    def get_context_data(self, parent_context=None):
        return asdict(self)
