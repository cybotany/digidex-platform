from django.urls import path
from apps.core.views import LinkingView, DigitizationView, LandingView, SignupUserView, LoginUserView, LogoutUserView, UserProfileView

app_name = 'core'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('link/<str:serial_number>/', LinkingView.as_view(), name='linking'),
    path('digitize/', DigitizationView.as_view(), name='digitization'),
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
