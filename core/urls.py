from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('internal/schema/', SpectacularAPIView.as_view(), name='internal-schema'),

    path('', SpectacularSwaggerView.as_view(url_name='internal-schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='internal-schema'), name='redoc'),

    path("", include("resume.urls"), name='resume'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
