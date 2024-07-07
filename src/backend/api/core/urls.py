from django.urls import path
from api.core.apiviews import Persona, ListPersona
urlpatterns = [
    
    path('get/Persona/<persona_id>/', Persona.as_view()),
    path('post/Persona/', Persona.as_view()),
    path('update/Persona/', Persona.as_view()),
    path('delete/Persona/<persona_id>/', Persona.as_view()),
    path('get/list/Persona/', ListPersona.as_view()),


]
