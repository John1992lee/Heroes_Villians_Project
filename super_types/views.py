from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import super_typeSerializer
from .models import super_type

@api_view()
def super_types(request):
    supers_types = request.query_params.get('type')
    super_types = super_types.objects.all()
    if supers_types:
            supers_types = super.filter(super__type=supers_types)
    serializer = super_typeSerializer(super_type)
    return Response(serializer.data)