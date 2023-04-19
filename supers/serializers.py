from rest_framework import serializers
from .models import super

class superSerializer(serializers.ModelSerializer):
    class Meta:
        model = super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1