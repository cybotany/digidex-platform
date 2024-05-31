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

#additional_urls = [
#    path('', views.add_category_view, name='add_category'),
#    path('<uuid:ntag_uuid>/', views.add_digit_view, name='add_digit'),
#]

profile_urls = [
    path('update/', views.update_profile_view, name='update_profile'),
    path('delete/', views.delete_profile_view, name='delete_profile'),
#    path('add/', include(additional_urls)),
    path('<slug:category_slug>/', include(category_urls)),
]

app_name = 'inventory'
urlpatterns = [
    path('<slug:user_slug>/', include(profile_urls)),
]
