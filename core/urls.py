"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from core import settings
from users.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="test API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('', list_view, name='list_view'),
                  path('create/', create_view, name='create_view'),
                  path('update/<pk>', update_view, name='update_view'),
                  path('delete/<pk>', delete_view, name='delete_view'),
                  path('admin/', admin.site.urls),
                  path('create-api/', UserCreateAPIView.as_view(), name='create_api'),
                  path('update-api/', UserUpdateAPIView.as_view(), name='update_api'),
                  path('delete-api/<pk>', UserDeleteAPIView.as_view(), name='delete_api'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
