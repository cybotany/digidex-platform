"""
cybotany URL Configuration
"""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.core.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='landing-page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('botany/', include('apps.botany.urls')),
    path('chatbot/', include('apps.chatbot.urls')),
    path('api/', include('apps.api.urls')),
    path('nfc/', include('apps.nfc.urls')),
    path('itis/', include('apps.itis.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)