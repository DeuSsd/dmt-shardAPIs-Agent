from rest_framework import serializers
#from .models import APIData
from .models import APIWEB


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = APIWEB
        fields = ('api', 'web_api')
