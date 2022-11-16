from rest_framework.views import APIView
from rest_framework.response import Response

from .models import postulantes
from.serializers import PostulanteSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class PostulanteView(APIView):
    
    def get(self,request):
        dataPostulantes = postulantes.objects.all()
        serPostulantes = PostulanteSerializer(dataPostulantes,many=True)
        return Response(serPostulantes.data)
    
    def post(self,request):
        serPostulantes = PostulanteSerializer(data=request.data)
        serPostulantes.is_valid(raise_exception=True)
        serPostulantes.save()
        
        return Response(serPostulantes.data)
    
class PostulanteDetailView(APIView):
    
    def get(self,request,postulantes_id):
        dataPostulante = postulantes.objects.get(pk=postulantes_id)
        serPostulantes = PostulanteSerializer(dataPostulante)
        return Response(serPostulantes.data)
    
    def put(self,request,postulantes_id):
        dataPostulante = postulantes.objects.get(pk=postulantes_id)
        serPostulantes = PostulanteSerializer(dataPostulante,data=request.data)
        serPostulantes.is_valid(raise_exception=True)
        serPostulantes.save()
        return Response(serPostulantes.data)
    
    def delete(self,request,postulantes_id):
        dataPostulante = postulantes.objects.get(pk=postulantes_id)
        serPostulantes = PostulanteSerializer(dataPostulante)
        dataPostulante.delete()
        return Response(serPostulantes.data)
