from rest_framework import serializers
from .models import super_type

class super_typeSerializer(serializers.ModelSerializer):
    class Meta:
        type = super_type
        fields = ['id', 'type']