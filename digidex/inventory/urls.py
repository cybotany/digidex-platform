from django.urls import path

from inventory.views import link_ntag_view, update_category_view, delete_category_view, update_digit_view, delete_digit_view

urlpatterns = [
    path('ntag/<uuid:ntag_uuid>/link', link_ntag_view, name='link_ntag'),

    path('category/<uuid:category_uuid>/update', update_category_view, name='update_category'),
    path('category/<uuid:category_uuid>/delete', delete_category_view, name='delete_category'),

    path('digit/<uuid:digit_uuid>/update', update_digit_view, name='update_digit'),
    path('digit/<uuid:digit_uuid>/delete', delete_digit_view, name='delete_digit'),
]
