from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pelicula
from .serializers import PeliculaSerializer


# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_url = {
        'List': '/lista',
        'Create': '/add',
        'Update': '/update',
        'Delete': '/delete',
    }
    return JsonResponse(api_url)


@api_view(['GET'])
def peliList(request):
    peliculas = Pelicula.objects.all()
    serializer = PeliculaSerializer(peliculas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def peliDetalle(request, pk):
    peliculas = Pelicula.objects.get(id=pk)
    serializer = PeliculaSerializer(peliculas, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def peliAdd(request):
    serializer = PeliculaSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)
