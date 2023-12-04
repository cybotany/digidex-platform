from django.urls import path
from apps.core.views import LinkingView, DigitizationView, GroupingView, InventoryView, SignupUserView, LoginUserView, LogoutUserView, UserProfileView

app_name = 'core'
urlpatterns = [
    path('', InventoryView.as_view(), name='landing'),
    path('link/<str:serial_number>/', LinkingView.as_view(), name='linking'),
    path('digitize/<int:link_id>/', DigitizationView.as_view(), name='digitization'),
    path('grouping/<int:group_id>/', GroupingView.as_view(), name='grouping'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
