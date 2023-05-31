from django.urls import path
from . import views

urlpatterns = [
    path('curso',views.Cursos),
    path('curso/registrarcurso',views.registrarcurso),
    path('curso/eliminarcurso/<codigo>',views.eliminarcurso),
    path('docente',views.Docentes),
    path('docente/registrardocente',views.registrardocente),
]