import posixpath

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.db.models import CharField, Prefetch, Q
from django.db.models.expressions import Exists, OuterRef
from django.db.models.functions import Cast, Length, Substr
from django.utils.translation import gettext_lazy as _

from wagtail.query import TreeQuerySet, SpecificQuerySetMixin
from wagtail.search.queryset import SearchableQuerySetMixin


class InventoryQuerySet(SearchableQuerySetMixin, SpecificQuerySetMixin, TreeQuerySet):
    def live_q(self):
        return Q(live=True)

    def live(self):
        """
        This filters the QuerySet to only contain published inventories.
        """
        return self.filter(self.live_q())

    def not_live(self):
        """
        This filters the QuerySet to only contain unpublished inventories.
        """
        return self.exclude(self.live_q())

    def in_menu_q(self):
        return Q(show_in_menus=True)

    def in_menu(self):
        """
        This filters the QuerySet to only contain inventories that are in the menus.
        """
        return self.filter(self.in_menu_q())

    def not_in_menu(self):
        """
        This filters the QuerySet to only contain inventories that are not in the menus.
        """
        return self.exclude(self.in_menu_q())

    def inventory_q(self, other):
        return Q(id=other.id)

    def inventory(self, other):
        """
        This filters the QuerySet so it only contains the specified inventory.
        """
        return self.filter(self.inventory_q(other))

    def not_inventory(self, other):
        """
        This filters the QuerySet so it doesn't contain the specified inventory.
        """
        return self.exclude(self.inventory_q(other))

    def type_q(self, *types):
        all_subclasses = {
            model for model in apps.get_models() if issubclass(model, types)
        }
        content_types = ContentType.objects.get_for_models(*all_subclasses)
        return Q(content_type__in=list(content_types.values()))

    def type(self, *types):
        """
        This filters the QuerySet to only contain inventories that are an instance
        of the specified model(s) (including subclasses).
        """
        return self.filter(self.type_q(*types))

    def not_type(self, *types):
        """
        This filters the QuerySet to exclude any inventories which are an instance of the specified model(s).
        """
        return self.exclude(self.type_q(*types))

    def exact_type_q(self, *types):
        content_types = ContentType.objects.get_for_models(*types)
        return Q(content_type__in=list(content_types.values()))

    def exact_type(self, *types):
        """
        This filters the QuerySet to only contain inventories that are an instance of the specified model(s)
        (matching the model exactly, not subclasses).
        """
        return self.filter(self.exact_type_q(*types))

    def not_exact_type(self, *types):
        """
        This filters the QuerySet to exclude any inventories which are an instance of the specified model(s)
        (matching the model exactly, not subclasses).
        """
        return self.exclude(self.exact_type_q(*types))

    def private_q(self):
        from .models import InventoryViewRestriction

        q = Q()
        for restriction in InventoryViewRestriction.objects.select_related("inventory").all():
            q |= self.descendant_of_q(restriction.inventory, inclusive=True)

        # do not match any inventory if no private section exists.
        return q if q else Q(pk__in=[])

    def public(self):
        """
        Filters the QuerySet to only contain inventories that are not in a private
        section and their descendants.
        """
        return self.exclude(self.private_q())

    def not_public(self):
        """
        Filters the QuerySet to only contain inventories that are in a private
        section and their descendants.
        """
        return self.filter(self.private_q())

    def private(self):
        """
        Filters the QuerySet to only contain inventories that are in a private
        section and their descendants.
        """
        return self.filter(self.private_q())

    def first_common_ancestor(self, include_self=False, strict=False):
        """
        Find the first ancestor that all inventories in this queryset have in common.
        For example, consider a inventory hierarchy like::

            - Home/
                - Foo Event Index/
                    - Foo Event Inventory 1/
                    - Foo Event Inventory 2/
                - Bar Event Index/
                    - Bar Event Inventory 1/
                    - Bar Event Inventory 2/

        The common ancestors for some queries would be:

        .. code-block:: python

            >>> Inventory.objects\\
            ...     .type(EventInventory)\\
            ...     .first_common_ancestor()
            <Inventory: Home>
            >>> Inventory.objects\\
            ...     .type(EventInventory)\\
            ...     .filter(title__contains='Foo')\\
            ...     .first_common_ancestor()
            <Inventory: Foo Event Index>

        This method tries to be efficient, but if you have millions of inventories
        scattered across your inventory tree, it will be slow.

        If `include_self` is True, the ancestor can be one of the inventories in the
        queryset:

        .. code-block:: python

            >>> Inventory.objects\\
            ...     .filter(title__contains='Foo')\\
            ...     .first_common_ancestor()
            <Inventory: Foo Event Index>
            >>> Inventory.objects\\
            ...     .filter(title__exact='Bar Event Index')\\
            ...     .first_common_ancestor()
            <Inventory: Bar Event Index>

        A few invalid cases exist: when the queryset is empty, when the root
        Inventory is in the queryset and ``include_self`` is False, and when there
        are multiple inventory trees with no common root (a case Wagtail does not
        support). If ``strict`` is False (the default), then the first root
        node is returned in these cases. If ``strict`` is True, then a
        ``ObjectDoesNotExist`` is raised.
        """
        # An empty queryset has no ancestors. This is a problem
        if not self.exists():
            if strict:
                raise self.model.DoesNotExist("Can not find ancestor of empty queryset")
            return self.model.get_first_root_node()

        if include_self:
            # Get all the paths of the matched inventories.
            paths = self.order_by().values_list("path", flat=True)
        else:
            # Find all the distinct parent paths of all matched inventories.
            # The empty `.order_by()` ensures that `Inventory.path` is not also
            # selected to order the results, which makes `.distinct()` works.
            paths = (
                self.order_by()
                .annotate(
                    parent_path=Substr(
                        "path",
                        1,
                        Length("path") - self.model.steplen,
                        output_field=CharField(max_length=255),
                    )
                )
                .values_list("parent_path", flat=True)
                .distinct()
            )

        # This method works on anything, not just file system paths.
        common_parent_path = posixpath.commonprefix(paths)

        # That may have returned a path like (0001, 0002, 000), which is
        # missing some chars off the end. Fix this by trimming the path to a
        # multiple of `Inventory.steplen`
        extra_chars = len(common_parent_path) % self.model.steplen
        if extra_chars != 0:
            common_parent_path = common_parent_path[:-extra_chars]

        if common_parent_path == "":
            # This should only happen when there are multiple trees,
            # a situation that Wagtail does not support;
            # or when the root node itself is part of the queryset.
            if strict:
                raise self.model.DoesNotExist("No common ancestor found!")

            # Assuming the situation is the latter, just return the root node.
            # The root node is not its own ancestor, so this is technically
            # incorrect. If you want very correct operation, use `strict=True`
            # and receive an error.
            return self.model.get_first_root_node()

        # Assuming the database is in a consistent state, this inventory should
        # *always* exist. If your database is not in a consistent state, you've
        # got bigger problems.
        return self.model.objects.get(path=common_parent_path)

    def unpublish(self):
        """
        This unpublishes all live inventories in the QuerySet.
        """
        for inventory in self.live():
            inventory.unpublish()

    def defer_streamfields(self):
        """
        Apply to a queryset to prevent fetching/decoding of StreamField values on
        evaluation. Useful when working with potentially large numbers of results,
        where StreamField values are unlikely to be needed. For example, when
        generating a sitemap or a long list of inventory links.
        """
        clone = self._clone()
        clone._defer_streamfields = True  # used by specific_iterator()
        streamfield_names = self.model.get_streamfield_names()
        if not streamfield_names:
            return clone
        return clone.defer(*streamfield_names)

    def in_site(self, site):
        """
        This filters the QuerySet to only contain inventories within the specified site.
        """
        return self.descendant_of(site.root_inventory, inclusive=True)

    def translation_of_q(self, inventory, inclusive):
        q = Q(translation_key=inventory.translation_key)

        if not inclusive:
            q &= ~Q(pk=inventory.pk)

        return q

    def translation_of(self, inventory, inclusive=False):
        """
        This filters the QuerySet to only contain inventories that are translations of the specified inventory.

        If inclusive is True, the inventory itself is returned.
        """
        return self.filter(self.translation_of_q(inventory, inclusive))

    def not_translation_of(self, inventory, inclusive=False):
        """
        This filters the QuerySet to only contain inventories that are not translations of the specified inventory.

        Note, this will include the inventory itself as the inventory is technically not a translation of itself.
        If inclusive is True, we consider the inventory to be a translation of itself so this excludes the inventory
        from the results.
        """
        return self.exclude(self.translation_of_q(inventory, inclusive))

    def prefetch_workflow_states(self):
        """
        Performance optimisation for listing inventories.
        Prefetches the active workflow states on each inventory in this queryset.
        Used by `workflow_in_progress` and `current_workflow_progress` properties on
        `wagtailcore.models.Inventory`.
        """
        from wagtail.models import WorkflowState

        workflow_states = WorkflowState.objects.active().select_related(
            "current_task_state__task"
        )

        relation = "_workflow_states"
        if self.is_specific:
            relation = "_specific_workflow_states"

        return self.prefetch_related(
            Prefetch(
                relation,
                queryset=workflow_states,
                to_attr="_current_workflow_states",
            )
        )

    def annotate_approved_schedule(self):
        """
        Performance optimisation for listing inventories.
        Annotates each inventory with the existence of an approved go live time.
        Used by `approved_schedule` property on `wagtailcore.models.Inventory`.
        """
        from wagtail.models import Revision

        return self.annotate(
            _approved_schedule=Exists(
                Revision.inventory_revisions.exclude(
                    approved_go_live_at__isnull=True
                ).filter(object_id=Cast(OuterRef("pk"), output_field=CharField()))
            )
        )
