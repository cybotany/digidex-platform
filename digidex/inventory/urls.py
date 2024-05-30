from django.urls import path

from inventory.views.category import link_ntag_view, update_category_view, delete_category_view, update_digit_view, delete_digit_view

urlpatterns = [
    path('ntag/<uuid:ntag_uuid>/link', link_ntag_view, name='link_ntag'),

    path('category/<uuid:category_uuid>/update', update_category_view, name='update_category'),
    path('category/<uuid:category_uuid>/delete', delete_category_view, name='delete_category'),

    path('digit/<uuid:digit_uuid>/update', update_digit_view, name='update_digit'),
    path('digit/<uuid:digit_uuid>/delete', delete_digit_view, name='delete_digit'),
]


from django.urls import path, include

from inventory.views.profile import update_account_view, delete_account_view

app_name = 'accounts'
urlpatterns = [
    path('inv/', include('inventory.urls')),
    path('<slug:user_slug>/update/', update_account_view, name='update_account'),
    path('<slug:user_slug>/delete/', delete_account_view, name='delete_account'),
]
