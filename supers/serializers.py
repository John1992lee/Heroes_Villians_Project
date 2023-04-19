from rest_framework import serializers
from .models import super

class superSerializer(serializers.ModelSerializer):
    class Meta:
        supers = super
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']