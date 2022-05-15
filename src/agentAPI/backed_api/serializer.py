from rest_framework import serializers
from .models import APIData


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = APIData
        fields = ('api', 'web_api')
