from rest_framework import serializers
from .models import *
class studSerializers(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.CharField()