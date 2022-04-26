from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Place, Rating

class PlaceSerializer(serializers.ModelSerializer):
    lat_lng = serializers.ReadOnlyField()
    lat = serializers.ReadOnlyField()
    long = serializers.ReadOnlyField()
    class Meta:
        model = Place
        fields = ('id','name','lat_lng','description','photo','location','lat','long')

class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'

class HybridSerializer(serializers.Serializer):
    place = serializers.CharField(max_length=300)
    user = serializers.IntegerField()