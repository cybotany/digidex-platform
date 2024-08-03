from wagtail import hooks

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PublishingPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from company.models import TeamMemberRole, Team

@hooks.register("register_icons")
def register_icons(icons):
    return icons + ['company/team.svg']

class TeamMemberRoleViewSet(SnippetViewSet):
    model = TeamMemberRole
    icon = "clipboard-list"
    menu_label = "Roles"
    menu_name = "roles"

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
    ]


class TeamViewSet(SnippetViewSet):
    model = Team
    icon = "team"
    menu_label = "Teams"
    menu_name = "teams"

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        InlinePanel('members', label="Members"),
    ]


class CompanyStaffViewSetGroup(SnippetViewSetGroup):
    items = (TeamMemberRoleViewSet, TeamViewSet)
    menu_icon = "globe"
    menu_label = "Staff"
    menu_name = "staff"


register_snippet(CompanyStaffViewSetGroup)