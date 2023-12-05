from django.urls import path
from apps.core.views import LandingView, LinkingView, DigitizationView, GroupingView, InventoryView, SignupUserView, LoginUserView, LogoutUserView

app_name = 'core'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('link/<str:serial_number>/', LinkingView.as_view(), name='linking'),
    path('digitize/<int:link_id>/', DigitizationView.as_view(), name='digitization'),
    path('grouping/<int:pk>/', GroupingView.as_view(), name='grouping'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
