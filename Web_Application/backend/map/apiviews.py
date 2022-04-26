from unicodedata import name
from rest_framework.response import Response
from .models import Place, Rating
from rest_framework import generics
from .serializers import HybridSerializer, PlaceSerializer,RatingSerializer
from rest_framework.views import APIView
import content_recommender, collaborative_recommender
from django.http import Http404
from tourist.models import User
from itertools import chain
import itinerary_recommender

class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceRecommend(APIView):
    def get_place(self,place):
        try:
            # obj = Place.objects.get(name=place)
            query = content_recommender.get_content_based_recommendations(place)
            place = Place.objects.filter(name__in=query).distinct()
            return place
        except:
            raise Http404

    def get(self, request, place, format=None):
        place = self.get_place(place)
        serializer = PlaceSerializer(place,many=True)
        return Response(serializer.data)

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CollaborativeRecommend(APIView):
    def get_collaborative_recommendation(self,pk):
        try:
            user = User.objects.get(id=pk)
            ratings_by_user = Rating.objects.all().filter(user_id=user).order_by('-rating')
            query = collaborative_recommender.recommender(ratings_by_user[0].id)
            place = Place.objects.filter(name__in=query).distinct()
            return place
        except:
            print("error eerrrro")
            raise Http404
        
    def get(self, request, pk, format=None):
        place = self.get_collaborative_recommendation(pk)
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)

class HybridRecommend(APIView):

    def get(self,request,format=None):
        HybridSerializer(data=request.data).is_valid(raise_exception=True)
        place_content = PlaceRecommend.get_place(self,place=request.data['place'])
        user_content = CollaborativeRecommend.get_collaborative_recommendation(self,pk=request.data['user'])
        result = list(chain(place_content,user_content))
        serializer = PlaceSerializer(result, many=True)
        return Response(serializer.data)

class ItineraryRecommend(APIView):

    def post(self,request,format=None):
        HybridSerializer(data=request.data).is_valid(raise_exception=True)

        user = User.objects.get(id=request.data['user'])
        ratings_by_user = Rating.objects.all().filter(user_id=user).order_by('-rating')
        places = collaborative_recommender.recommender(ratings_by_user[0].id)

        place_content = content_recommender.get_content_based_recommendations(request.data['place'])
        result = place_content + places
        query = itinerary_recommender.recommend(result)
        places = []
        for i in query:
            try:
                place = Place.objects.get(name=i)
                if place:
                    print(place)
                    places.append(place)
            except:
                pass
            
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

