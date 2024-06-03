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

profile_urls = [
    path('<slug:category_slug>/', include(category_urls)),
]

app_name = 'inventory'
urlpatterns = [
    path('link/<uuid:ntag_uuid>/', views.add_digit_view, name='add_digit'),
    path('<slug:user_slug>/', include(profile_urls)),
]
