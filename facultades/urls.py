from django.urls import path, include
from rest_framework import routers
from facultades import views


router = routers.DefaultRouter()
router.register(r'academias',views.AcademiaViewSet)
router.register(r'profesor',views.ProfesorViewSet)
router.register(r'alumno',views.AlumnoViewSet)
router.register(r'curso',views.CursoViewSet)
router.register(r'nota',views.NotaViewSet)
router.register(r'alumnos_cursos',views.AlumnoCursoViewSet)

urlpatterns = [
    path('',include(router.urls))
]