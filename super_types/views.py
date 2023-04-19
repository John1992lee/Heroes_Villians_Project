from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import super_typeSerializer
from .models import super_type

@api_view()
def super_types(request):
    super_types = super_types.objects.all()
    serializer = super_typeSerializer(super_type)
    return Response(serializer.data)