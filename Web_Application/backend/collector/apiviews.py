from .models import Log 
from rest_framework import generics
from .serializers import LogSerializer
from django.db.models import Count
from map.models import Place
from rest_framework.views import APIView
from rest_framework.response import Response
from map.serializers import PlaceSerializer
from map.models import Place


class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

def PopularityBasedRecs(num=6):    
    items = Log.objects.values('content_id')
    items = items.filter(event='buy').annotate(Count('user_id'))
    sorted_items = sorted(items, key=lambda item: -float(item['user_id__count']))
    return sorted_items[:num]

def chart(take=10):
    sorted_items = PopularityBasedRecs(take)
    print(sorted_items)
    places = []
    for i in sorted_items:
        places.append(Place.objects.get(id=i['content_id']))
    print(places)
    return places

class PopularityRecommend(APIView):
    def get(self,request,format=None):
        place = chart()
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)
