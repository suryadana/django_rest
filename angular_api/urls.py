"""angular_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

API_VERSION = 'v1'
schema_view = get_schema_view(
    openapi.Info(
        title="Angular API",
        default_version=API_VERSION,
        description="""

        This is documentation of Angular API

        """,
        terms_of_service="",
        contact=openapi.Contact(email="suryadana@brahmanactf.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
	path('api/' + API_VERSION + '/', include('authentication.urls'), name='api'),
]
