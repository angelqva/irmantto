"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from user.urls import user_router, logout_router
from cliente.urls import cliente_router, equipo_router
from empresa.urls import empresa_router, responsables_router
from trabajador.urls import trabajador_router

schema_view = get_schema_view(
    openapi.Info(
        title="IRMANTTO APIREST",
        default_version='v1',
        description="Django, DjangoRestFramework, Postgres, SimpleJWT",
        terms_of_service="https://github.com/angelqva/irmantto",
        contact=openapi.Contact(email="angel.napolesqva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/login/', TokenObtainPairView.as_view(), name='token_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', include(logout_router.urls)),
    # routes api from apps
    path('api/', include(user_router.urls)),
    path('api/', include(cliente_router.urls)),
    path('api/', include(equipo_router.urls)),
    path('api/', include(empresa_router.urls)),
    path('api/', include(responsables_router.urls)),
    path('api/', include(trabajador_router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
