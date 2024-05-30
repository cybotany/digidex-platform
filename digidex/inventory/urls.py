from django.urls import path, include

from inventory import views

digit_urls = [
    path('update/', views.update_digit_view, name='update_digit'),
    path('delete/', views.delete_digit_view, name='delete_digit'),
]

category_urls = [
    path('update/', views.update_category_view, name='update_category'),
    path('delete/', views.delete_category_view, name='delete_category'),
    path('<slug:digit_slug>/', include(digit_urls)),
]

ntag_urls = [
    path('<uuid:ntag_uuid>', views.link_ntag_view, name='link_ntag'),
]

profile_urls = [
    path('update/', views.update_profile_view, name='update_profile'),
    path('delete/', views.delete_profile_view, name='delete_profile'),
    path('ntag/', include(ntag_urls)),
    path('<slug:category_slug>/', include(category_urls)),
]

app_name = 'inventory'
urlpatterns = [
    path('<slug:profile_slug>/', include(profile_urls)),
]
