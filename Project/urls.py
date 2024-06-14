"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg import openapi
from Project import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view

from Main.views import (RegisterAPIview, LoginAPIview,
                         LogoutAPIview, UserProfilAPIview, home)


schema_view = get_schema_view(
    openapi.Info(
        title="Online Course Platform (OCP) API",
        default_version='v1',
        description="This Api about free courses, and everyone can see for freely.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@local.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/v1/', include('Main.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('register/', RegisterAPIview.as_view(), name='register'),
    path('login/', LoginAPIview.as_view(), name='login'),
    path('log-out/', LogoutAPIview.as_view(), name='log-out'),
    path('profile/', UserProfilAPIview.as_view(), name='profile'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)