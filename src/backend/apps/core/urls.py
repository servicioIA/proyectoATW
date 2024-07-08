from django.urls import path, include
from apps.core import views
from .views import importar_preguntas
from .views import importar_datos_entrenamiento
from .views import chat, reiniciar_conversacion


urlpatterns = [
    path('', views.index, name='index'),
    path('importar_preguntas/', importar_preguntas, name='importar_preguntas'),
    path('importar_datos_entrenamiento/', importar_datos_entrenamiento, name='importar_datos_entrenamiento'),
    path('chat/', chat, name='chat'),
    path('reiniciar_conversacion/', reiniciar_conversacion, name='reiniciar_conversacion'),
]


