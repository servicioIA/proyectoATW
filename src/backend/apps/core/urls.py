from django.urls import path, include
from apps.core import views

urlpatterns = [
    path('', views.index, name='index')
]