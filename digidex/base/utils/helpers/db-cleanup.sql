--SELECT * FROM public.django_migrations WHERE django_migrations.app = 'home'
--ORDER BY id ASC ;

--SELECT * FROM public.django_content_type WHERE django_content_type.app_label = 'home'
--ORDER BY id ASC;

--SELECT * FROM public.auth_permission WHERE auth_permission.content_type_id in (37, 62)
--ORDER BY id ASC;

SELECT * FROM public.wagtailcore_pagelogentry WHERE wagtailcore_pagelogentry.content_type_id in (37, 62)
ORDER BY id ASC;