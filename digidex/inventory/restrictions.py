from wagtail.models import BaseViewRestriction

class PageViewRestriction(BaseViewRestriction):
    page = models.ForeignKey(
        "Page",
        verbose_name=_("page"),
        related_name="view_restrictions",
        on_delete=models.CASCADE,
    )

    passed_view_restrictions_session_key = "passed_page_view_restrictions"

    class Meta:
        verbose_name = _("page view restriction")
        verbose_name_plural = _("page view restrictions")

    def save(self, user=None, **kwargs):
        """
        Custom save handler to include logging.
        :param user: the user add/updating the view restriction
        :param specific_instance: the specific model instance the restriction applies to
        """
        specific_instance = self.page.specific
        is_new = self.id is None
        super().save(**kwargs)

        if specific_instance:
            log(
                instance=specific_instance,
                action="wagtail.view_restriction.create"
                if is_new
                else "wagtail.view_restriction.edit",
                user=user,
                data={
                    "restriction": {
                        "type": self.restriction_type,
                        "title": force_str(
                            dict(self.RESTRICTION_CHOICES).get(self.restriction_type)
                        ),
                    }
                },
            )

    def delete(self, user=None, **kwargs):
        """
        Custom delete handler to aid in logging
        :param user: the user removing the view restriction
        """
        specific_instance = self.page.specific
        if specific_instance:
            removed_restriction_type = PageViewRestriction.objects.filter(
                id=self.id
            ).values_list("restriction_type", flat=True)[0]
            log(
                instance=specific_instance,
                action="wagtail.view_restriction.delete",
                user=user,
                data={
                    "restriction": {
                        "type": self.restriction_type,
                        "title": force_str(
                            dict(self.RESTRICTION_CHOICES).get(removed_restriction_type)
                        ),
                    }
                },
            )
        return super().delete(**kwargs)