from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import materiaView,syllabusFile

router = DefaultRouter()

router.register(r'materias', materiaView, basename="materias")

urlpatterns = [
    path('',include(router.urls)),
    path('syllabus/', syllabusFile.as_view())
]

