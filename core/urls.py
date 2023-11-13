from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="UzChess",
        default_version='v1',
        description="API for UzChess",
        contact=openapi.Contact(email="eralideveloper@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = i18n_patterns(
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/news/', include('news.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/library/', include('library.urls')),
    path('api/v1/course/', include('course.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
