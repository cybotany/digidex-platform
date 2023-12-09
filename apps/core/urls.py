from django.urls import path
from apps.core.views import (ContactUsView,
                             AboutUsView,
                             DigitView,
                             LandingView,
                             LinkingView,
                             DigitizationView,
                             GroupedDigitsView,
                             GardenView,
                             SignupUserView,
                             LoginUserView,
                             LogoutUserView)

app_name = 'core'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('garden/', GardenView.as_view(), name='garden'),
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('company/', AboutUsView.as_view(), name='company'),
    path('link/<str:serial_number>/', LinkingView.as_view(), name='linking'),
    path('digitize/<int:link_id>/', DigitizationView.as_view(), name='digitization'),
    path('digit/<int:pk>/', DigitView.as_view(), name='digit'),
    path('grouped_digits/<int:group_id>/', GroupedDigitsView.as_view(), name='grouped-digits'),
]
