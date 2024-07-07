from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import socket

HOSTNAME = ""
try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

schema_view = get_schema_view(
   openapi.Info(
      title="Labs API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   # url="https://"+HOSTNAME+"/api"
)
urlpatterns = [
    # auth
    path('', include('rest_framework.urls'), name='rest_framework'),
    # Apiviews
    path('core/', include('api.core.urls')),
    # swagger docs
    path('docs/', schema_view.as_view())
]
