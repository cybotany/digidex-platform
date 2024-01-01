from django.urls import path
from .views import (SignupUserView, LoginUserView, LogoutUserView)

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
