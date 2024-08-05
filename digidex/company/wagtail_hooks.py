from wagtail import hooks

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PublishingPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from company.models import TeamMemberRole, TeamMember, Team

@hooks.register("register_icons")
def register_icons(icons):
    return icons + ['company/icons/team.svg', 'company/icons/badge.svg']

class TeamMemberViewSet(SnippetViewSet):
    model = TeamMember
    icon = "badge"
    menu_label = "Employees"
    menu_name = "employees"

    panels = [
        FieldPanel('user'),
        FieldPanel('role'),
        FieldPanel('image'),
    ]


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
        InlinePanel('members', label="Member"),
    ]


class CompanyStaffViewSetGroup(SnippetViewSetGroup):
    items = (TeamMemberViewSet, TeamMemberRoleViewSet, TeamViewSet)
    menu_icon = "globe"
    menu_label = "Staff"
    menu_name = "staff"


register_snippet(CompanyStaffViewSetGroup)