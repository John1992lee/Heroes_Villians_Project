from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import superSerializer
from .models import super

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = super.objects.all()
        serializer = superSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = superSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_description(request, pk):
    supers = get_object_or_404(super, pk=pk)
    if request.method == 'GET':
        serializer = superSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = superSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
