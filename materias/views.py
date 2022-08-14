from ast import Raise
from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework import mixins
from rest_framework.views import APIView
from django.http import FileResponse

from .serializers import materiaSerializer
from .models import materia
from rest_framework.response import Response

# Create your views here.
from catalogoPensum.settings import BASE_DIR
import os



class materiaView(
    viewsets.ModelViewSet
    ):
    serializer_class =  materiaSerializer
    queryset = materia.objects.all()


class syllabusFile(APIView):
    
    def post(self,request,*args,**kwargs):
        
        carrera = request.data.get("carrera" , "")
        codigo = request.data.get("codigo", "")

        ruta = os.path.join(BASE_DIR,"src","syllabus", carrera+codigo+".pdf")

        try:
            return FileResponse(open(ruta,"rb"))
        except:
            return raiseExceptions

        

