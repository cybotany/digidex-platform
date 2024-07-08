from dataclasses import dataclass, asdict
from laces.components import Component

from base.components import Section, Block, Heading, Paragraph
from inventory.models import UserProfile


@dataclass
class Category(Component):
    template_name = 'inventory/components/category.html'

    name: str
    description: str

    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class CategoriesBlock(Block):
    def get_context_data(self, parent_context=None):
        return asdict(self)


@dataclass
class Dashboard(Component):
    template_name = 'inventory/components/dashboard.html'

    children: list[Component]

    @classmethod
    def from_user(cls, user):
        user_profile = UserProfile.objects.select_related('inventory').get(user__id=user.id)
        user_inventory = user_profile.inventory

        categories = CategoriesBlock.from_user_inventory(user)
        block = Block(
            children=[
                Heading(text='Block Heading', size=1, style='top'),
                categories,
            ],
            style='top'
        )
        content = Section(
            children=[
                block,
            ],
            style='top'
        )
        
        descendants = user_inventory.get_children()
        if descendants.exists():
            categories = descendants.filter(_type='c')
            items = descendants.filter(_type='i')
            
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            profile_image_url=user.profile.image.url,
        )

    def get_context_data(self, parent_context=None):
        return asdict(self)
