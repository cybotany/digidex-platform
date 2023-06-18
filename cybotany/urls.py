"""
cybotany URL Configuration
"""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.core.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('apps.authentication.urls')),
    path('botany/', include('apps.botany.urls')),
    path('cea/', include('apps.cea.urls')),
    path('chatbot/', include('apps.chatbot.urls')),
    path('api/', include('apps.api.urls')),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
