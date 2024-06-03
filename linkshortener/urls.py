from django.urls import include, path
from django.contrib import admin

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Link Shorneter App",
        default_version='v1',
        description="API Docs",
        #   terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="medinamaria90@gmail.com"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
    path('apidocs<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('apidocs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('', include('redirects.urls')),
]
