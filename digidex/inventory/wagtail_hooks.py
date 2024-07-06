from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from inventory.models import Inventory, Category, Item, Link

class InventoryViewSet(SnippetViewSet):
    model = Inventory
    icon = 'folder-open-inverse'
    list_display = ('name', 'created_at', 'last_modified')
    search_fields = ('name', 'body')
    fields = ('name', 'body')


register_snippet(Category)
register_snippet(Item)
